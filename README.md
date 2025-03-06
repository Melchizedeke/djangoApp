# Blog Application

A Django-based blog application that allows users to create, view, update, and delete posts. This application features user authentication, pagination, and the ability to view posts by specific users.

## Features

- User authentication (login required for viewing and managing posts)
- Main post listing page showing all posts
- User-specific post pages
- Post detail view
- Create, update, and delete post functionality
- User permission checks for editing and deleting posts
- Pagination (5 posts per page)
- Posts displayed in reverse chronological order (newest first)
- About page

## Views

The application includes the following views:

### PostListView

Displays all posts on the home page, ordered by most recent first:

```python
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-date_posted']
```

### UserPostListView

Displays posts from a specific user, also ordered by most recent first:

```python
class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
```

### PostDetailView

Displays a single post's details:

```python
class PostDetailView(DetailView):
    model = Post
```

### PostCreateView

Allows authenticated users to create new posts:

```python
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

### PostUpdateView

Allows users to update their own posts:

```python
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
```

### PostDeleteView

Allows users to delete their own posts:

```python
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
```

### About Page

A simple about page for the application:

```python
@login_required
def about(request):
    return render(request, "blog/about.html", {'title':'About'})
```

## Setup

1. Clone this repository
2. Install the required dependencies
3. Run database migrations
4. Start the Django development server

## Requirements

- Django
- Python 3.x
- Django's authentication system

## Usage

After setting up the application:

1. Register as a new user or log in with existing credentials
2. View all posts on the home page
3. Navigate to a specific user's posts by clicking on their username
4. Use the pagination controls to browse through posts
5. Create your own posts
6. Edit or delete your posts as needed
7. View the about page to learn more about the application

## Models

The application relies on the following models:

- `Post`: Stores blog post content with fields for title, content, author, and date_posted
- `User`: Django's built-in user model for authentication

## Security Features

- Login required for viewing posts and the about page
- Users can only edit and delete their own posts
- UserPassesTestMixin ensures permission checks for update and delete operations