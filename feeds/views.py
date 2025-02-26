# feeds/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Feed
from .forms import FeedForm
from django.http import JsonResponse
from animals.models import Animal
from django.contrib import messages





def add_feed(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed_list')  # After saving, redirect to feed list page
    else:
        form = FeedForm()

    return render(request, 'feeds/add_feed.html', {'form': form})

def feed_list(request):
    feeds = Feed.objects.all()

    context = {
        'feeds': feeds
    }
    return render(request, 'feeds/feed_list.html', context)

def get_animal_tags_by_category(request):
    category = request.GET.get('category')
    animals = Animal.objects.filter(category=category)
    tag_numbers = [animal.tag_number for animal in animals]

    return JsonResponse(tag_numbers, safe=False)


def edit_feed(request, feed_id):
    feed = get_object_or_404(Feed, id=feed_id)  # Fetch the feed by its ID
    if request.method == "POST":
        form = FeedForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            messages.success(request, "Feed updated successfully!")
            return redirect('feed_list')  # Redirect to the feed list page after updating
    else:
        form = FeedForm(instance=feed)  # Populate the form with existing data

    return render(request, 'feeds/edit_feed.html', {'form': form, 'feed': feed})



# feeds/views.py
def delete_feed(request, feed_id):
    feed = get_object_or_404(Feed, id=feed_id)  # Fetch the feed by ID
    feed.delete()
    messages.success(request, "Feed deleted successfully!")
    return redirect('feed_list')  # Redirect back to feed list page after deletion
