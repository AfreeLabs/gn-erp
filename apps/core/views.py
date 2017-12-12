from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.user.is_authenticated():
        return home(request)
    else:
        return render(request, 'core/login.html')

@login_required
def home(request):
    return render(request, 'core/home.html')




 # <table class="table table-bordered table-sm">
 #                    <thead>
 #                        <tr>
 #                        <!-- <th><input class="form-check-input" type="checkbox" value=""></th> -->
 #                        <th scope="col">N<sup>o</sup></th>
 #                        <th>Date de payement</th>
 #                        <th>Nom de l'Etudiant</th>
 #                        <th>Matricule de l'Etudiant</th>
 #                        <th>Type de frais</th>
 #                        <th>montant</th>
 #                     </tr>
 #                    </thead>
 #                    <tbody>
 #                    <tr>
 #                        {% for payement in student.registree.registration_payement.all %}
 #                       <!--  <td scope="row">{{forloop.counter}}</td> -->
 #                       <td scope="row">{{ student.id }}</td>
 #                        <td>{{payement.date|date:"DATE_FORMAT" }}</td>
 #                        <td>{{student.registree}}</td>
 #                        <td>
 #                            <a href="" class="">{{student.matricule}}
 #                            </a>
                            
 #                        </td>
                       
 #                        <td>{{ payement.payement_type }}</td>
 #                        <td>{{ payement.amount}}</td>
 #                        {% endfor %}

 #                    </tr>

 #                    </tbody>
        
 #                  </table>