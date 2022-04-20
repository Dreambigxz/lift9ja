from variables import *

def delete_user_top_up_data(request):

    data = request.GET['data']
    data = TopUpHistory.objects.get(user=request.user, id=data)
    data.delete()
    messages.success(request, 'Data history successfully deleted.')
    return reverse('/dashboard')
