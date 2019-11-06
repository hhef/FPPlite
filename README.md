# FPPlite - Portfolio Project #1
> This application is for warehouse management

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
This app is my portfolio project after programming bootcamp. This is a summary
of what I learned in the course

## Technologies
* Python 3.7
* Django 2.2.6
* psycopg2-binary 2.8.3

## Setup
Create new virtualenv and install everything from requirements.txt. If you want
to use other database than this in this project, run populate_sript.py after migrate

## Code Examples
```python
def post(self, request):
    contractors = Contractor.objects.order_by('name')
    form = ContractorForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/contractors")
    else:
        return render(request, "contractors.html", {"form": form,
                                                    "contractors": contractors})
```

## Features
List of features ready and TODOs for future development
* You can add products, edit them, select by category.
* In warehouse you can search products by name or code.
* You can add contractors and edit them

To-do list:
* Sales
* Delivery

## Status
Project is _in progress_. I'm also doing other projects for my portfolio but I hope
I'll come back to this

## Inspiration
This is a lite version of a program I was using on my first job in wholesaler's

## Contact
Created by [@hef](https://twitter.com/hef4rl) - feel free to contact me!