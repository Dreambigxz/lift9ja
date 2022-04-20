from variables import *
import os

def check_fake_uploads():

    # how to get all fake uploads
    """
    get all approved gold dats, print where all file name exist or greater than 1 and the user
    """
    files = ['logo_nato.gif', 'IMG-20220205-WA0008.jpg']
    approved_gs = UserGold.objects.filter(state='approved', filtered=False).exclude(proof_name__in=files)
    print(len(approved_gs))
    file_list = []

    count = 0
    for i in approved_gs:
        proofs = os.path.basename(i.proof.name)
        if proofs != '':
            i.proof_name = proofs
            i.save()

            # print('Checking prof name:', proofs, i.proof_name)
            try:
                proofs = UserGold.objects.get(proof_name=proofs)
            except:
                print(i, 'CHEATED with file name', proofs)

def unblock():
    users = MyUser.objects.filter(is_blocked=True)
    for i in users:
        i.is_blocked = False
        i.save()