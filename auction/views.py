from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Team, Player
from django.core.paginator import Paginator
from .forms import AuctionForm
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    return render(request, 'auction/home.html', {
        'teams': teams,
        'players': players,
    })

@login_required
def clubs(request):
    clubs = Team.objects.all()
    return render(request, 'auction/clubs.html', {'clubs': clubs})

@login_required
def team_detail(request, team_id):
    team_obj = get_object_or_404(Team, id=team_id)
    players = team_obj.players.all()  
    captain = team_obj.captain 

    return render(request, 'auction/team_detail.html', {
        'team': team_obj,
        'players': players,
        'captain': captain,
    })

@login_required
def players(request):
    players_list = Player.objects.all().order_by(Lower('name'))
    paginator = Paginator(players_list, 15)
    page_number = request.GET.get('page')
    players = paginator.get_page(page_number)

    return render(request, 'auction/player.html', {'players': players})


@login_required
def auction(request, player_id):
    # Teams sorted alphabetically
    teams = Team.objects.all().order_by(Lower('team_name'))
    current_player = get_object_or_404(Player, id=player_id)

    # Player is considered sold if it already has a team
    is_sold = current_player.team is not None
    # Safe check: True only if this player is set as some team's captain
    is_captain = hasattr(current_player, 'captain_of_team')


    if request.method == 'POST':
        # -----------------------------
        # ADMIN: UNSMELL / MAKE UNSOLD
        # -----------------------------
        if 'unsell_player' in request.POST:
            if request.user.is_staff and is_sold:
                team = current_player.team
                sold_price = current_player.sold_price or 0

                # ✅ Refund selling price back to team purse
                if team and sold_price:
                    team.purse_remaining += sold_price
                    team.save()

                # Make player unsold
                current_player.team = None
                current_player.sold_price = None
                current_player.save()

            return redirect('auction', player_id=player_id)

        # -----------------------------
        # ADMIN: REMOVE PLAYER
        # -----------------------------
        if 'delete_player' in request.POST:
            if request.user.is_staff:
                current_player.delete()
                return redirect('players')  # your players list URL name
            return redirect('auction', player_id=player_id)

        # -----------------------------
        # NORMAL BID SUBMISSION
        # -----------------------------
        # If already sold, do NOT allow another sale
        if is_sold:
            return redirect('auction', player_id=player_id)

        form = AuctionForm(request.POST)
        if form.is_valid():
            selected_team = form.cleaned_data.get('team')
            price = form.cleaned_data.get('price')

            if selected_team and price and selected_team.purse_remaining >= price:
                current_player.team = selected_team

                # ✅ Store sold price
                current_player.sold_price = price
                current_player.save()

                # Deduct from purse
                selected_team.purse_remaining -= price
                selected_team.save()

                return redirect('assigned', player_id=player_id, team_id=selected_team.id)
    else:
        form = AuctionForm()

    context = {
        'player': current_player,
        'form': form,
        'teams': teams,
        'is_sold': is_sold,
        'is_captain':is_captain,
    }
    return render(request, 'auction/auction.html', context)

@login_required
def assigned(request, player_id, team_id):
    player = get_object_or_404(Player, id=player_id)
    club = get_object_or_404(Team, id=team_id)

    return render(request, 'auction/assigned.html', {
        'player': player,
        'club': club,
    })
