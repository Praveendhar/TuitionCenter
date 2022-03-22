from django.shortcuts import render

def index_accounts(request):
    return render(request,'index_accounts.html')
def accounts_dashboard(request):
    return render(request,'accounts_dashboard.html')