from django.shortcuts import redirect, render, get_object_or_404
from .models import Tweet
from .forms import TweetForm, UserRegistration
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login





def tweet_list(req):
    tweets = Tweet.objects.all().order_by("-created_at")

    return render(req, "tweet_list.html", {"tweets": tweets})


@login_required
def create_tweet(req):
    if req.method == "POST":

        form_data = TweetForm(req.POST, req.FILES)
        if form_data.is_valid():
            tweet = form_data.save(commit=False)
            tweet.user = req.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm()

    return render(req, "create_tweet_form.html", {"form": form})


@login_required
def edit_tweet(req, tweet_id):

    tweet = get_object_or_404(Tweet, pk=tweet_id, user=req.user)

    if req.method == "POST":
        form_data = TweetForm(req.POST, req.FILES, instance=tweet)
        if form_data.is_valid():

            # We can do the same and ignore them as well
            # tweet = form_data.save(commit=False)
            # tweet.user = req.user
            # tweet.save()

            tweet = form_data.save()
            return redirect("tweet_list")

    else:
        form = TweetForm(instance=tweet)

    return render(req, "create_tweet_form.html", {"form": form})


@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweet_delete.html", {"tweet": tweet})


def userRegistration(req):
    if req.method == "POST":
        form = UserRegistration(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(req, user)
            return redirect("tweet_list")
    else:
        form = UserRegistration()

    return render(req, "registration/registration.html", {"form": form})
