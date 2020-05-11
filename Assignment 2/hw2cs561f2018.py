import copy
f = open("input.txt")

def add_arr(arr1, arr2):
    arr3 = copy.deepcopy(arr1)
    for i in range(7):
        arr3[i] += arr2[i]
    return arr3

def subtract_arr(arr1, arr2):
    arr3 = copy.deepcopy(arr1)
    for i in range(7):
        arr3[i] -= arr2[i]
    return arr3

def is_valid_move(array1, array2, max):
    for i in range(7):
        if array1[i] + array2[i] > max:
            return False
    return True

def intersection_turn(spla_moves, lahsa_moves, spla_spots, lahsa_beds, played):
    global p, b
    blahsa_score = [0, 0, 0, 0, 0, 0, 0]
    bspla_score = [0, 0, 0, 0, 0, 0, 0]
    id = ""
    iPlayed = False

    for spla_selected in spla_moves:
        if is_valid_move(spla_selected.days, spla_spots, p):
            index1 = spla_moves.index(spla_selected)
            index2 = 0
            flag1 = False
            iPlayed = True
            spla_moves.remove(spla_selected)
            if spla_selected in lahsa_moves:
                flag1 = True
                index2 = lahsa_moves.index(spla_selected)
                lahsa_moves.remove(spla_selected)
            if len(spla_moves) + len(lahsa_moves) == 0:
                spla_moves.insert(index1, spla_selected)
                if flag1:
                    lahsa_moves.insert(index2, spla_selected)
                return spla_selected.days, [0, 0, 0, 0, 0, 0, 0], spla_selected.applicantID
            spla_days, lahsa_days, lahsa_chosen_ap_id = lahsa_turn(spla_moves, lahsa_moves,
                                                                   add_arr(spla_spots, spla_selected.days), lahsa_beds,
                                                                   True)
            if flag1:
                lahsa_moves.insert(index2, spla_selected)
            spla_moves.insert(index1, spla_selected)
            if sum(add_arr(spla_days, spla_selected.days)) > sum(bspla_score):
                bspla_score = add_arr(spla_days, spla_selected.days)
                blahsa_score = lahsa_days
                id = spla_selected.applicantID
    if not iPlayed and played:
        return lahsa_turn(spla_moves, lahsa_moves, spla_spots, lahsa_beds, iPlayed)
    elif not iPlayed and not played:
        return [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], ''
    return bspla_score, blahsa_score, id

def spla_turn(spla_moves, lahsa_moves, spla_spots, lahsa_beds, played):
    global p, b
    blahsa_score = [0, 0, 0, 0, 0, 0, 0]
    bspla_score = [0, 0, 0, 0, 0, 0, 0]
    id = ""
    iPlayed=False

    for spla_selected in spla_moves:
        if is_valid_move(spla_selected.days, spla_spots, p):
            index1 = spla_moves.index(spla_selected)
            index2 = 0
            flag1 = False
            iPlayed=True
            spla_moves.remove(spla_selected)
            if spla_selected in lahsa_moves:
                flag1 = True
                index2 = lahsa_moves.index(spla_selected)
                lahsa_moves.remove(spla_selected)
            if len(spla_moves) + len(lahsa_moves) == 0:
                spla_moves.insert(index1, spla_selected)
                if flag1:
                    lahsa_moves.insert(index2, spla_selected)
                return spla_selected.days, [0, 0, 0, 0, 0, 0, 0], spla_selected.applicantID
            spla_days, lahsa_days, lahsa_chosen_ap_id = lahsa_turn(spla_moves, lahsa_moves,
                                                                   add_arr(spla_spots, spla_selected.days), lahsa_beds,True)
            if flag1:
                lahsa_moves.insert(index2, spla_selected)
            spla_moves.insert(index1, spla_selected)
            if sum(add_arr(spla_days, spla_selected.days)) > sum(bspla_score):
                bspla_score = add_arr(spla_days, spla_selected.days)
                blahsa_score = lahsa_days
                id = spla_selected.applicantID
    if not iPlayed and played:
        return lahsa_turn(spla_moves,lahsa_moves,spla_spots,lahsa_beds,iPlayed)
    elif not iPlayed and not played:
        return [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],''
    return bspla_score, blahsa_score, id


def lahsa_turn(spla_moves2, lahsa_moves2, spla_spots2, beds_filled2,played):
    global b
    blahsa_score2 = [0, 0, 0, 0, 0, 0, 0]
    bspla_score2 = [0, 0, 0, 0, 0, 0, 0]
    id = ""
    iPlayed = False
    for lahsa_selected in lahsa_moves2:
        if is_valid_move(lahsa_selected.days, beds_filled2, b):
            flag2 = False
            index1 = lahsa_moves2.index(lahsa_selected)
            index2 = 0
            iPlayed=True
            if lahsa_selected in spla_moves2:
                flag2 = True
                index2 = spla_moves2.index(lahsa_selected)
                spla_moves2.remove(lahsa_selected)
            lahsa_moves2.remove(lahsa_selected)
            if len(spla_moves2) + len(lahsa_moves2) == 0:
                lahsa_moves2.insert(index1, lahsa_selected)
                if flag2:
                    spla_moves2.insert(index2, lahsa_selected)
                return  lahsa_selected.days, [0, 0, 0, 0, 0, 0, 0], lahsa_selected.applicantID
            spla_days, lahsa_days, spla_chosen_ap_id = spla_turn(spla_moves2, lahsa_moves2, spla_spots2,
                                                                 add_arr(beds_filled2, lahsa_selected.days),True)
            if flag2:
                spla_moves2.insert(index2, lahsa_selected)
            lahsa_moves2.insert(index1, lahsa_selected)
            if sum(add_arr(lahsa_days, lahsa_selected.days)) > sum(blahsa_score2) :
                blahsa_score2 = add_arr(lahsa_days, lahsa_selected.days)
                bspla_score2 = spla_days
                id = lahsa_selected.applicantID
    if not iPlayed and played:
        return spla_turn(spla_moves2,lahsa_moves2,spla_spots2,beds_filled2,iPlayed)
    elif not iPlayed and not played:
        return [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],''
    return bspla_score2, blahsa_score2, id

class Applicant:

    def __init__(self, applicantID, gender, age, pets, medical_conditions, car, drivers_license, days):
        self.applicantID = applicantID
        self.gender = gender
        self.age = age
        self.pets = pets
        self.medical_conditions = medical_conditions
        self.car = car
        self.drivers_license = drivers_license
        self.days = days
global b,p
b = int(f.readline().strip())
p = int(f.readline().strip())
L = int(f.readline().strip())
lahsa_preselected = []
for x in range(L):
    lahsa_preselected.append(f.readline().strip())
S = int(f.readline().strip())
spla_preselected = []
for x in range(S):
    spla_preselected.append(f.readline().strip())
A = int(f.readline().strip())

spla_only = []
lahsa_only = []
intersection = []

spla_parking_space_init = [0, 0, 0, 0, 0, 0, 0]
lahsa_beds_init = [0, 0, 0, 0, 0, 0, 0]

for x in range(A):
    applicant = f.readline().strip()
    if applicant[:5] in spla_preselected:
        for i in range(7):
            if applicant[i + 13] == "1":
                spla_parking_space_init[i] += 1
        continue
    if applicant[:5] in lahsa_preselected:
        for i in range(7):
            if applicant[i + 13] == "1":
                lahsa_beds_init[i] += 1
        continue
    if applicant[10] == "N" and applicant[11] == "Y" and applicant[12] == "Y":
        if applicant[5] == "F" and int(applicant[6:9]) > 17 and applicant[9] == "N":
            intersection.append(
                Applicant(applicant[:5], applicant[5], applicant[6:9], applicant[9], applicant[10],
                          applicant[11], applicant[12],
                          [int(applicant[13]), int(applicant[14]), int(applicant[15]),
                           int(applicant[16]), int(applicant[17]), int(applicant[18]), int(applicant[19])]))
        else:
            spla_only.append(
                Applicant(applicant[:5], applicant[5], applicant[6:9], applicant[9], applicant[10],
                          applicant[11], applicant[12],
                          [int(applicant[13]), int(applicant[14]), int(applicant[15]),
                           int(applicant[16]), int(applicant[17]), int(applicant[18]), int(applicant[19])]))
    elif applicant[5:6] == "F" and int(applicant[6:9]) > 17 and applicant[9] == "N":
        lahsa_only.append(
            Applicant(applicant[:5], applicant[5], applicant[6:9], applicant[9], applicant[10],
                      applicant[11], applicant[12], [int(applicant[13]), int(applicant[14]), int(applicant[15]),
                                                           int(applicant[16]), int(applicant[17]), int(applicant[18]),
                                                           int(applicant[19])]))
spla_sol, lahsa_sol, ans = spla_turn(intersection + spla_only, intersection + lahsa_only,
                spla_parking_space_init, lahsa_beds_init,True)

o = open("output.txt", "w")
o.write(ans)
o.write('\n')
o.close()