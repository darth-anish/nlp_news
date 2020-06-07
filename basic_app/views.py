from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, ListView
from .forms import PostForm
from basic_app.extras.nlp_preprocess import tok,preprocess_stop_words,max_length
from tensorflow.keras.preprocessing import sequence
import numpy as np
from tensorflow.keras.models import load_model
from .models import Post
from django.utils import timezone

model = load_model('basic_app/programs_folder/Model_LSTM.h5py')
# Create your views here.

def index(request):

    return render(request,'index.html')

def predict(request):

    var1 = request.POST['var']
    labels=['business','entertainment','politics','sport','tech']

    def predict_res(sample):
        sam_list = sample.split()
        test = preprocess_stop_words(sam_list)
        testing = tok.texts_to_sequences([test])
        sam_seq = sequence.pad_sequences(testing, maxlen=max_length)
        res = model.predict(sam_seq)
        return labels[np.argmax(res)]

    pred_class = predict_res(var1)

    return render(request, 'basic_app/predict.html', {'Predicted':pred_class})

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class CreatePostView(CreateView):
    redirect_field_name = 'post_detail.html'

    form_class = PostForm
    model = Post

class PostDetailView(DetailView):
    model = Post

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()

    return redirect('post_detail', pk=post.pk)
