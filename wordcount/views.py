from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html',{'hi_there':'This is me'})

def count(request):
	full_text = request.GET['fulltext']
	wordlist = full_text.split()
	word_dict = {}
	for word in wordlist:
		if word in word_dict:
			word_dict[word] += 1
		else:
			word_dict[word] = 1
	dict_list = word_dict.items()
	dict_list = sorted(dict_list,key = operator.itemgetter(1), reverse = True)

	return render(request,'count.html',{'fulltext':full_text,
		'count': len(wordlist), 'worddict':dict_list})