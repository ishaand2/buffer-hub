from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from admin.user.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model, logout
from django.contrib.auth import login as auth_login
from admin.homepage.models import Homepage
from django.db import connection
from django_globals import globals
from rest_framework.response import Response
from django.http import JsonResponse
import uuid
import re

# Create your views here.
quality_points = {
	"A+" : 4/4,
	"A" : 4/4,
	"A-" : 3.67/4,
	"B+" : 3.33/4,
	"B" : 3.0/4,
	"B-" : 2.67/4,
	"C+" : 2.33/4,
	"C" : 2.00/4,
	"C-" : 1.67/4,
	"D+" : 1.33/4,
	"D" : 1.00/4,
	"D-" : 0.67/4,
	"F" : 0/4
}

def index(request):

	data = Homepage.objects.all()

	return render(request, 'frontendTemplates/home/index.html', {'data':data})

def demo_insert(request):
	if request.method == 'POST':
		info = {}
		info['email_Id'] = request.POST['email_Id']
		info['Course_Comb'] = request.POST['Course_Comb']
		info['Letter_Grade'] = request.POST['Letter_Grade']
		info['GPA_Hours'] = float(request.POST['GPA_Hours'])
		info['_id'] = str(uuid.uuid1())
		#print(type(info['GPA_Hours']))
		#print(quality_points[info['Letter_Grade']])
		info['GPA_QUALITY_POINTS'] = info['GPA_Hours'] * quality_points[info['Letter_Grade']]

		with connection.cursor() as cursor:
			cursor.execute("Insert Into Student_Course_Table(_id, email_Id, Course_Comb, Letter_Grade, GPA_HOURS, GPA_QUALITY_POINTS) Values (%s, %s, %s, %s, %s, %s)",
            [info['_id'], info["email_Id"], info["Course_Comb"], info["Letter_Grade"], info["GPA_Hours"], info["GPA_QUALITY_POINTS"]])

		messages.success(request, 'Entry Successful')
		#return info
		info['status'] = "Success"
		return JsonResponse(info)
	return

def demo_query(request):
	if request.method == 'POST':
		info = {}
		info['email_Id'] = request.POST['email_Id']
		result = None
		with connection.cursor() as cursor:
			cursor.execute("Select * From Student_Course_Table Where email_Id = %s ;",[info['email_Id']])
			#cursor.fetchone()
			result = cursor.fetchall()
		messages.success(request, 'Entry Successful')
		output = {}
		output['results'] = []
		result_list = list(result)
		output['status'] = 'Failure'
		for entry in result_list:
			temp = {}
			temp['email_Id'] = entry[0]
			temp['_id'] = entry[1]
			temp['Course_Comb'] = entry[2]
			temp['Letter_Grade'] = entry[3]
			temp['GPA_HOURS'] = entry[4]
			temp['GPA_QUALITY_POINTS'] = entry[5]
			output['results'].append(temp)
			output['status'] = 'Success'

		return JsonResponse(output)
	return

def demo_update(request):
	if request.method == 'POST':
		info = {}
		info['email_Id'] = request.POST['email_Id']
		info['Course_Comb'] = request.POST['Course_Comb']
		info['Letter_Grade'] = request.POST['Letter_Grade']
		#info['GPA_Hours'] = float(request.POST['GPA_Hours'])
		result = {}
		result['status'] = 'Failure'
		with connection.cursor() as cursor:
			cursor.execute("Select * From Student_Course_Table Where email_Id = %s  and Course_Comb = %s ;",
			[info['email_Id'],info['Course_Comb']])
			temp = cursor.fetchone()
			print("Update result:")
			print(temp)
			if temp == None:
				messages.error(request, 'Invalid Entry')
				return
			info['GPA_QUALITY_POINTS'] = float(temp[4]) * quality_points[info['Letter_Grade']]
			cursor.execute('''Update Student_Course_Table
			Set Course_Comb = %s, Letter_Grade = %s, GPA_QUALITY_POINTS = %s
			Where _id = %s;''',
            [info["Course_Comb"], info["Letter_Grade"], info["GPA_QUALITY_POINTS"], temp[1]])
			# result = cursor.fetchall()
			# print(result)
			result['status'] = 'Success'
		messages.success(request, 'Update Successful')
		return JsonResponse(result)
	return

def demo_delete(request):
	if request.method == 'POST':
		info = {}
		info['email_Id'] = request.POST['email_Id']
		info['Course_Comb'] = request.POST['Course_Comb']
		result = {}
		result['status'] = 'Failure'
		with connection.cursor() as cursor:
			cursor.execute("Delete From Student_Course_Table Where email_Id = %s  and Course_Comb = %s ;",
				[info['email_Id'], info['Course_Comb']])
			#cursor.fetchone()
			result['status'] = 'Success'
		messages.success(request, 'Delete Successful')
		return JsonResponse(result)
	return

def signup(request):
	return render(request, 'frontendTemplates/signup/index.html')

def demo_site(request):
	return render(request, 'frontendTemplates/demo_page.html')

def signup_post(request):
	if request.method == 'POST':
		f_name = request.POST['fname']
		l_name = request.POST['lname']
		email_Id = request.POST['email_id']
		password= request.POST['password']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',f_name):

			messages.error(request, 'Enter a valid Name')
			return redirect('home-signup')
		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',l_name):

			messages.error(request, 'Enter a valid Name')
			return redirect('home-signup')

		if not re.match('^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$',email_Id):

			messages.error(request, 'Enter a valid Email')
			return redirect('home-signup')


		usr = CustomUser(first_name=f_name, last_name=l_name, username = email_Id,password=make_password(password), )

		usr.save()
		# with connection.cursor() as cursor:
		# 	cursor.execute("Insert Into User_Accounts(email_Id, password, fname, lname) Values (%s, %s, %s, %s)",
        #     [new_user["email_Id"], new_user["password"], new_user["fname"], new_user["lname"]])

		messages.success(request, 'Successfully Registered!')
		return redirect('home-login')

def login(request):
	return render(request, 'frontendTemplates/login/index.html')


def login_post(request):
	user = {}
	user['username'] = request.POST['email']
	user['password'] = request.POST['password']
	username= request.POST['email']
	password = request.POST['password']
	if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", user['username']):
		messages.error(request, 'Enter a valid Email')
		return redirect('home-login')

	if len(user['password']) < 3:
		messages.error(request, 'Provide a Valid Password')
		return redirect('home-login')
	UserModel = get_user_model()
	try:
		user = UserModel.objects.get(username=username)


		if user.check_password(password):
			auth_login(request, user)
			return redirect('home-index')
		else:
			return redirect('home-login')
	except UserModel.DoesNotExist:
		messages.error(request, 'Invalid Email!')
		return redirect('home-login')
	# with connection.cursor() as cursor:
	# 	#cursor.execute("Select * From User_Accounts Where email_Id = "+user['username']+"and password = "+user['password'])
	# 	cursor.execute("Select * from User_Accounts where email_Id = %s and password = %s",
    #                     [user["username"], user["password"]]
    #     )
	# 	result = cursor.fetchone()
	# 	print(result)
	# 	if result == None:
	# 		messages.error(request, 'Invalid Login!')
	# 		return redirect('home-login')
	# 	#auth_login(request, user)
	# 	return redirect('home-index')

	# UserModel = get_user_model()
	# try:
	# 	user = UserModel.objects.get(email=username)

	# 	if user.check_password(password):
	# 		auth_login(request, user)
	# 		return redirect('home-index')
	# 	else:
	# 		messages.error(request, 'Invalid Password!')
	# 		return redirect('home-login')

	# except UserModel.DoesNotExist:
	# 	messages.error(request, 'Invalid Email!')
	# 	return redirect('home-login')

@login_required(login_url='home-login')
def logout_post(request):
    logout(request)
    return redirect('home-index')
