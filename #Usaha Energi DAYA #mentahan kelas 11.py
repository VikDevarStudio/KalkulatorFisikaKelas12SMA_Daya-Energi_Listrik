# Usaha Energi DAYA
import json


def main():
    while True:
        print("1. Sign Up")
        print("2. Login")
        print("3. Quit/End")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            signup(username, password)
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if login(username, password):
                perform_operations()
                break
            else:
                print("Invalid username or password. Please try again.")
        elif choice == '3':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def signup(username, password):
    user_data = load_user_data()

    if username in user_data:
        print("Username already exists. Please choose a different username.")
    else:
        user_data[username] = {'password': password}
        save_user_data(user_data)
        print("Signup successful. You can now login.")


def login(username, password):
    user_data = load_user_data()

    if username in user_data and user_data[username]['password'] == password:
        print("Login successful. Welcome, {}!".format(username))
        set_user_authenticated(True)
        return True
    else:
        set_user_authenticated(False)
        return False


def save_user_data(data):
    with open('user_data.json', 'w') as file:
        json.dump(data, file)


def load_user_data():
    try:
        with open('user_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def set_user_authenticated(value):
    with open('auth_status.txt', 'w') as file:
        file.write(str(value))


def is_user_authenticated():
    try:
        with open('auth_status.txt', 'r') as file:
            return file.read() == 'True'
    except FileNotFoundError:
        return False


def perform_operations():
    print("Welcome! Sekarang Anda Dapat Mengakses 3 Opsi Dibawah Ini:")
    print("1. Physhics Calculator")
    print("2. Logout")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        kakulatorfisik()
    elif choice == '2':
        logout()
    else:
        print("Invalid choice. Please enter 1, or 2.")


def kakulatorfisik():
    # Replace this with code to display user profile information
    quests1 = ["1", "2", "3"]
    energi1 = ["1", "2", "3", "4", "5"]
    Daya1 = ["1", "2", "3", "4", "5"]
    usaha1 = ["1", "2"]
    massalist = ["1", "2", "3", "4", "5", "6", "7", "8"]
    velolist = ["1", "2", "3", "4", "5", "6", "7"]
    dislist = ["1", "2", "3", "4", "5", "6", "7"]

    print("="*50)
    print("Grade 11 Pyhsics Calculator")
    print("Calculator STARTED!")
    print("-Masukkan Angka Saja Untuk Memilih Opsi yang Tersedia")
    print("="*50)

    while True:
        quest1 = str(input("Mau Hitung Apa? (1. Usaha, 2. Energi, 3. Daya): "))
        if quest1 not in quests1:
            print("Weklkom bek!")
            quest1 = str(
                input("Mau Hitung Apa? (1. Usaha, 2. Energi, 3. Daya): "))

        if quest1 == "2":

            Energi = str(
                input("1. EK, 2. DeltaEK, 3. EP, 4. DeltaEP, 5. EM: "))
            while Energi not in energi1:
                print("Input Salah Ya Wir!")
                Energi = str(
                    input("1. EK, 2. DeltaEK, 3. EP, 4. DeltaEP, 5. EM: "))
            if Energi == "1":
                massac = str(input(
                    "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                while massac not in massalist:
                    print("Satuan Yang Anda Masukkan Salah")
                    massac = str(input(
                        "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                massak = float(
                    input("Masukkan Massanya(Hanya Angka, Contoh = 5): "))
                if massac == "1":
                    mas = massak * 1000
                elif massac == "2":
                    mas = massak
                elif massac == "3":
                    mas = massak / 10
                elif massac == "4":
                    mas = massak / 100
                elif massac == "5":
                    mas = massak / 1000
                elif massac == "6":
                    mas = massak / 10000
                elif massac == "7":
                    mas = massak / 100000
                elif massac == "8":
                    mas = massak / 1000000
                else:
                    print("Maaf Input Salah!")

                VeloMT = str(
                    input("Kecepatan Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while VeloMT not in velolist:
                    print("Satuan Yang Anda Masukkan Salah")
                    VeloMT = str(
                        input("Kecepatan Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                velo = float(
                    input("Masukkan Kecepatannya(Hanya Angka, Contoh = 15): "))
                if VeloMT == "1":
                    vel = velo * 1000
                elif VeloMT == "2":
                    vel = velo * 100
                elif VeloMT == "3":
                    vel = velo * 10
                elif VeloMT == "4":
                    vel = velo
                elif VeloMT == "5":
                    vel = velo / 10
                elif VeloMT == "6":
                    vel = velo / 100
                elif VeloMT == "7":
                    vel = velo / 1000
                else:
                    print("Maaf Input Salah!")

                EK = 1/2 * mas * (vel**2)
                print("Energi Kinetiknya Adalah : ", EK, "Joule")

            elif Energi == "2":
                massac = str(input(
                    "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                while massac not in massalist:
                    print("Satuan Yang Anda Masukkan Salah")
                    massac = str(input(
                        "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                massak = float(
                    input("Masukkan Massanya(Hanya Angka, Contoh = 5): "))
                if massac == "1":
                    mas = massak * 1000
                elif massac == "2":
                    mas = massak
                elif massac == "3":
                    mas = massak / 10
                elif massac == "4":
                    mas = massak / 100
                elif massac == "5":
                    mas = massak / 1000
                elif massac == "6":
                    mas = massak / 10000
                elif massac == "7":
                    mas = massak / 100000
                elif massac == "8":
                    mas = massak / 1000000
                else:
                    print("Maaf Input Salah!")

                VeloMT = str(
                    input("Kecepatan Pertama Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while VeloMT not in velolist:
                    print("Satuan Yang Anda Masukkan Salah")
                    VeloMT = str(
                        input("Kecepatan Pertama Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                velo1 = float(
                    input("Masukkan Kecepatannya Pertamanya(Hanya Angka, Contoh = 10): "))
                if VeloMT == "1":
                    vel1 = velo1 * 1000
                elif VeloMT == "2":
                    vel1 = velo1 * 100
                elif VeloMT == "3":
                    vel1 = velo1 * 10
                elif VeloMT == "4":
                    vel1 = velo1
                elif VeloMT == "5":
                    vel1 = velo1 / 10
                elif VeloMT == "6":
                    vel1 = velo1 / 100
                elif VeloMT == "7":
                    vel1 = velo1 / 1000
                else:
                    print("Maaf Input Salah!")

                VeloMT = str(
                    input("Kecepatan Pertama Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while VeloMT not in velolist:
                    print("Satuan Yang Anda Masukkan Salah")
                    VeloMT = str(
                        input("Kecepatan Kedua Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                velo2 = float(
                    input("Masukkan Kecepatannya Keduanya(Hanya Angka, Contoh = 15): "))
                if VeloMT == "1":
                    vel2 = velo2 * 1000
                elif VeloMT == "2":
                    vel2 = velo2 * 100
                elif VeloMT == "3":
                    vel2 = velo2 * 10
                elif VeloMT == "4":
                    vel2 = velo2
                elif VeloMT == "5":
                    vel2 = velo2 / 10
                elif VeloMT == "6":
                    vel2 = velo2 / 100
                elif VeloMT == "7":
                    vel2 = velo2 / 1000
                else:
                    print("Maaf Input Salah!")

                ΔEK = (1/2 * massak * vel1**2)-(1/2 * massak * vel2**2)
                print("ΔEnergi Kinetiknya Adalah : ", ΔEK, "Joule")

            elif Energi == "3":
                massac = str(input(
                    "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                while massac not in massalist:
                    print("Satuan Yang Anda Masukkan Salah")
                    massac = str(input(
                        "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                massak = float(
                    input("Masukkan Massanya(Hanya Angka, Contoh = 5): "))
                if massac == "1":
                    mas = massak * 1000
                elif massac == "2":
                    mas = massak
                elif massac == "3":
                    mas = massak / 10
                elif massac == "4":
                    mas = massak / 100
                elif massac == "5":
                    mas = massak / 1000
                elif massac == "6":
                    mas = massak / 10000
                elif massac == "7":
                    mas = massak / 100000
                elif massac == "8":
                    mas = massak / 1000000
                else:
                    print("Maaf Input Salah!")
                disMT = str(input(
                    "Ketinggian Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while disMT not in dislist:
                    print("Satuan Yang Anda Masukkan Salah")
                    disMT = str(input(
                        "Ketinggian Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                dis = float(
                    input("Masukkan Ketinggiannya(Hanya Angka, Contoh = 10): "))
                if disMT == "1":
                    hei = dis * 1000
                elif disMT == "2":
                    hei = dis * 100
                elif disMT == "3":
                    hei = dis * 10
                elif disMT == "4":
                    hei = dis
                elif disMT == "5":
                    hei = dis / 10
                elif disMT == "6":
                    hei = dis / 100
                elif disMT == "7":
                    hei = dis / 1000
                else:
                    print("Maaf Input Salah!")
                EP = mas * 10 * hei
                print("Energi Potensialnya Adalah : ", EP, "Joule")

            elif Energi == "4":
                massac = str(input(
                    "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                while massac not in massalist:
                    print("Satuan Yang Anda Masukkan Salah")
                    massac = str(input(
                        "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                massak = float(
                    input("Masukkan Massa nya(Hanya Angka, Contoh = 5): "))
                if massac == "1":
                    mas = massak * 1000
                elif massac == "2":
                    mas = massak
                elif massac == "3":
                    mas = massak / 10
                elif massac == "4":
                    mas = massak / 100
                elif massac == "5":
                    mas = massak / 1000
                elif massac == "6":
                    mas = massak / 10000
                elif massac == "7":
                    mas = massak / 100000
                elif massac == "8":
                    mas = massak / 1000000
                else:
                    print("Maaf Input Salah!")

                disMT = str(input(
                    "Ketinggian Pertama Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while disMT not in dislist:
                    print("Satuan Yang Anda Masukkan Salah")
                    disMT = str(input(
                        "Ketinggian Pertama Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                dis = float(
                    input("Masukkan Ketinggian Pertamanya(Hanya Angka, Contoh = 15): "))
                if disMT == "1":
                    hei1 = dis * 1000
                elif disMT == "2":
                    hei1 = dis * 100
                elif disMT == "3":
                    hei1 = dis * 10
                elif disMT == "4":
                    hei1 = dis
                elif disMT == "5":
                    hei1 = dis / 10
                elif disMT == "6":
                    hei1 = dis / 100
                elif disMT == "7":
                    hei1 = dis / 1000
                else:
                    print("Maaf Input Salah!")

                disMT = str(input(
                    "Ketinggian Kedua Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while disMT not in dislist:
                    print("Satuan Yang Anda Masukkan Salah")
                    disMT = str(input(
                        "Ketinggian Kedua Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                dis = float(
                    input("Masukkan Ketinggian Keduanya(Hanya Angka, Contoh = 10): "))
                if disMT == "1":
                    hei2 = dis * 1000
                elif disMT == "2":
                    hei2 = dis * 100
                elif disMT == "3":
                    hei2 = dis * 10
                elif disMT == "4":
                    hei2 = dis
                elif disMT == "5":
                    hei2 = dis / 10
                elif disMT == "6":
                    hei2 = dis / 100
                elif disMT == "7":
                    hei2 = dis / 1000
                else:
                    print("Maaf Input Salah!")

                ΔEP = (mas * 10 * hei1)-(mas * 10 * hei2)
                print("ΔEnergi Potensialnya Adalah : ", ΔEP, "Joule")

            elif Energi == "5":
                massac = str(input(
                    "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                while massac not in massalist:
                    print("Satuan Yang Anda Masukkan Salah")
                    massac = str(input(
                        "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                massak = float(
                    input("Masukkan Massa nya(Hanya Angka, Contoh = 10): "))
                if massac == "1":
                    mas = massak * 1000
                elif massac == "2":
                    mas = massak
                elif massac == "3":
                    mas = massak / 10
                elif massac == "4":
                    mas = massak / 100
                elif massac == "5":
                    mas = massak / 1000
                elif massac == "6":
                    mas = massak / 10000
                elif massac == "7":
                    mas = massak / 100000
                elif massac == "8":
                    mas = massak / 1000000
                else:
                    print("Maaf Input Salah!")
                VeloMT = str(
                    input("Kecepatan Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while VeloMT not in velolist:
                    print("Satuan Yang Anda Masukkan Salah")
                    VeloMT = str(
                        input("Kecepatan Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                velo = float(
                    input("Masukkan Kecepatannya(Hanya Angka, Contoh = 10): "))
                if VeloMT == "1":
                    vel = velo * 1000
                elif VeloMT == "2":
                    vel = velo * 100
                elif VeloMT == "3":
                    vel = velo * 10
                elif VeloMT == "4":
                    vel = velo
                elif VeloMT == "5":
                    vel = velo / 10
                elif VeloMT == "6":
                    vel = velo / 100
                elif VeloMT == "7":
                    vel = velo / 1000
                else:
                    print("Maaf Input Salah!")
                disMT = str(input(
                    "Ketinggian Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while disMT not in dislist:
                    print("Satuan Yang Anda Masukkan Salah")
                    disMT = str(input(
                        "Ketinggian Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                dis = float(
                    input("Masukkan Ketinggiannya(Hanya Angka, Contoh = 15): "))
                if disMT == "1":
                    hei = dis * 1000
                elif disMT == "2":
                    hei = dis * 100
                elif disMT == "3":
                    hei = dis * 10
                elif disMT == "4":
                    hei = dis
                elif disMT == "5":
                    hei = dis / 10
                elif disMT == "6":
                    hei = dis / 100
                elif disMT == "7":
                    hei = dis / 1000
                else:
                    print("Maaf Input Salah!")
                EKK = 1/2 * massak * vel
                EPP = massak * 10 * hei
                EM = EKK + EPP
                print("Energi Kinetik Nya Adalah: ", EKK, "Joule")
                print("Energi Potensial Nya Adalah: ", EPP, "Joule")
                print("Energi Mekaniknya Adalah: ", EM, "Joule")
            else:
                print("Maaf Input Salah!")
        elif quest1 == "1":
            Usaha = str(
                input("Pilih Rumus Usahanya(1. FxS, 2. FxSxCosTeta): "))
            while Usaha not in usaha1:
                print("Input Salah Ya Wir!")
                Usaha = str(
                    input("Pilih Rumus Usahanya(1. FxS, 2. FxSxCosTeta): "))

            if Usaha == "1":
                F = float(input("Masukkan Gaya Nya(Hanya Angka, Contoh = 5): "))
                disMT = str(input(
                    "Jarak Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while disMT not in dislist:
                    print("Satuan Yang Anda Masukkan Salah")
                    disMT = str(
                        input("Jarak Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                dis = float(
                    input("Masukkan Jaraknya(Hanya Angka, Contoh = 10): "))
                if disMT == "1":
                    jar = dis * 1000
                elif disMT == "2":
                    jar = dis * 100
                elif disMT == "3":
                    jar = dis * 10
                elif disMT == "4":
                    jar = dis
                elif disMT == "5":
                    jar = dis / 10
                elif disMT == "6":
                    jar = dis / 100
                elif disMT == "7":
                    jar = dis / 1000
                else:
                    print("Maaf Input Salah!")
                fs = F * jar
                print("Usaha Nya Adalah: ", fs, "Joule")
            elif Usaha == "2":
                F1 = float(
                    input("Masukkan Gaya Nya(Hanya Angka, Contoh = 5): "))
                disMT = str(input(
                    "Jarak Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while disMT not in dislist:
                    print("Satuan Yang Anda Masukkan Salah")
                    disMT = str(
                        input("Jarak Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                dis = float(
                    input("Masukkan Jaraknya(Hanya Angka, Contoh = 10): "))
                if disMT == "1":
                    jar = dis * 1000
                elif disMT == "2":
                    jar = dis * 100
                elif disMT == "3":
                    jar = dis * 10
                elif disMT == "4":
                    jar = dis
                elif disMT == "5":
                    jar = dis / 10
                elif disMT == "6":
                    jar = dis / 100
                elif disMT == "7":
                    jar = dis / 1000
                else:
                    print("Maaf Input Salah!")
                fs = F1 * jar
                teta = float(
                    input("Masukkan Teta Nya (1. 0, 2. 30, 3. 45, 4. 60, 5. 90): "))
                while teta not in [1, 2, 3, 4, 5]:
                    print("Maaf, input salah!")
                    teta = float(
                        input("Masukkan Teta Nya (1. 0, 2. 30, 3. 45, 4. 60, 5. 90): "))
                if teta == 1:
                    teta1 = 1
                elif teta == 2:
                    teta1 = 0.8660254037844
                elif teta == 3:
                    teta1 = 0.7071067811865
                elif teta == 4:
                    teta1 = 0.5
                elif teta == 5:
                    teta1 = 0
                else:
                    print("Maaf Input Salah!")
                fscost = F1 * jar * teta1
                print("Usaha Nya Adalah: ", fscost, "Joule")
            else:
                print("Maaf Input Salah!")
        elif quest1 == "3":
            Daya = str(input(
                "Pilihlah Rumus Dayanya(1. DayaFS, 2. DayaFSCos, 3. DayaEK, 4. DayaEP, 5. DayaEM): "))
            while Daya not in Daya1:
                print("Input Salah Ya wir!")
                Daya = str(input(
                    "Pilihlah Rumus Dayanya(1. DayaFS, 2. DayaFSCos, 3. DayaEK, 4. DayaEP, 5. DayaEM): "))
            if Daya == "1":
                Df = float(
                    input("Masukkan Gaya Nya(Hanya Angka, Contoh = 5): "))
                disMT = str(input(
                    "Jarak Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while disMT not in dislist:
                    print("Satuan Yang Anda Masukkan Salah")
                    disMT = str(input(
                        "Jarak Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                dis = float(
                    input("Masukkan Jaraknya(Hanya Angka, Contoh = 10): "))
                if disMT == "1":
                    jar = dis * 1000
                elif disMT == "2":
                    jar = dis * 100
                elif disMT == "3":
                    jar = dis * 10
                elif disMT == "4":
                    jar = dis
                elif disMT == "5":
                    jar = dis / 10
                elif disMT == "6":
                    jar = dis / 100
                elif disMT == "7":
                    jar = dis / 1000
                else:
                    print("Maaf Input Salah!")
                t = float(input("Masukkan Waktu Nya: "))
                Dfs = (Df * dis) / t
                print("Daya Nya Adalah: ", Dfs, "Watt")
            elif Daya == "2":
                Df1 = float(
                    input("Masukkan Gaya Nya(Hanya Angka, Contoh = 5): "))
                disMT = str(input(
                    "Jarak Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while disMT not in dislist:
                    print("Satuan Yang Anda Masukkan Salah")
                    disMT = str(input(
                        "Jarak Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                dis = float(
                    input("Masukkan Jaraknya(Hanya Angka, Contoh = 10): "))
                if disMT == "1":
                    jar = dis * 1000
                elif disMT == "2":
                    jar = dis * 100
                elif disMT == "3":
                    jar = dis * 10
                elif disMT == "4":
                    jar = dis
                elif disMT == "5":
                    jar = dis / 10
                elif disMT == "6":
                    jar = dis / 100
                elif disMT == "7":
                    jar = dis / 1000
                else:
                    print("Maaf Input Salah!")
                Dteta = float(
                    input("Masukkan Teta Nya (1. 0, 2. 30, 3. 45, 4. 60, 5. 90): "))
                while Dteta not in [1, 2, 3, 4, 5]:
                    print("Maaf, input salah!")
                    Dteta = float(
                        input("Masukkan Teta Nya (1. 0, 2. 30, 3. 45, 4. 60, 5. 90): "))
                if Dteta == 1:
                    Dteta1 = 1
                elif Dteta == 2:
                    Dteta1 = 0.8660254037844
                elif Dteta == 3:
                    Dteta1 = 0.7071067811865
                elif Dteta == 4:
                    Dteta1 = 0.5
                elif Dteta == 5:
                    Dteta1 = 0
                else:
                    print("Maaf Input Salah!")
                t1 = float(input("Masukkan Waktu Nya: "))
                Dfsc = (Df1 * dis * Dteta1) / t1
                print("Daya Nya Adalah: ", Dfsc, "Watt")
            elif Daya == "3":
                massac = str(input(
                    "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                while massac not in massalist:
                    print("Satuan Yang Anda Masukkan Salah")
                    massac = str(input(
                        "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                massak = float(
                    input("Masukkan Massanya(Hanya Angka, Contoh = 5): "))
                if massac == "1":
                    mas = massak * 1000
                elif massac == "2":
                    mas = massak
                elif massac == "3":
                    mas = massak / 10
                elif massac == "4":
                    mas = massak / 100
                elif massac == "5":
                    mas = massak / 1000
                elif massac == "6":
                    mas = massak / 10000
                elif massac == "7":
                    mas = massak / 100000
                elif massac == "8":
                    mas = massak / 1000000
                else:
                    print("Maaf Input Salah!")
                VeloMT = str(
                    input("Kecepatan Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while VeloMT not in velolist:
                    print("Satuan Yang Anda Masukkan Salah")
                    VeloMT = str(
                        input("Kecepatan Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                velo = float(
                    input("Masukkan Kecepatannya(Hanya Angka, Contoh = 15): "))
                if VeloMT == "1":
                    vel = velo * 1000
                elif VeloMT == "2":
                    vel = velo * 100
                elif VeloMT == "3":
                    vel = velo * 10
                elif VeloMT == "4":
                    vel = velo
                elif VeloMT == "5":
                    vel = velo / 10
                elif VeloMT == "6":
                    vel = velo / 100
                elif VeloMT == "7":
                    vel = velo / 1000
                else:
                    print("Maaf Input Salah!")
                t2 = float(input("Masukkan Waktu Nya: "))
                Dek = (1/2 * massak * (vel ** 2))/t2
                print("Daya Nya Adalah: ", Dek, "Watt")
            elif Daya == "4":
                massac = str(input(
                    "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                while massac not in massalist:
                    print("Satuan Yang Anda Masukkan Salah")
                    massac = str(input(
                        "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                massak = float(
                    input("Masukkan Massanya(Hanya Angka, Contoh = 5): "))
                if massac == "1":
                    mas = massak * 1000
                elif massac == "2":
                    mas = massak
                elif massac == "3":
                    mas = massak / 10
                elif massac == "4":
                    mas = massak / 100
                elif massac == "5":
                    mas = massak / 1000
                elif massac == "6":
                    mas = massak / 10000
                elif massac == "7":
                    mas = massak / 100000
                elif massac == "8":
                    mas = massak / 1000000
                else:
                    print("Maaf Input Salah!")
                disMT = str(input(
                    "Ketinggian Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while disMT not in dislist:
                    print("Satuan Yang Anda Masukkan Salah")
                    disMT = str(input(
                        "Ketinggian Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                dis = float(
                    input("Masukkan Ketinggiannya(Hanya Angka, Contoh = 10): "))
                if disMT == "1":
                    hei = dis * 1000
                elif disMT == "2":
                    hei = dis * 100
                elif disMT == "3":
                    hei = dis * 10
                elif disMT == "4":
                    hei = dis
                elif disMT == "5":
                    hei = dis / 10
                elif disMT == "6":
                    hei = dis / 100
                elif disMT == "7":
                    hei = dis / 1000
                else:
                    print("Maaf Input Salah!")
                t3 = float(input("Masukkan Waktu Nya: "))
                Dep = (massak * 10 * hei) / t3
                print("Daya Nya Adalah: ", Dep, "Watt")
            elif Daya == "5":
                massac = str(input(
                    "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                while massac not in massalist:
                    print("Satuan Yang Anda Masukkan Salah")
                    massac = str(input(
                        "Massa Mu Dalam Satuan Apa? (1. Ton, 2. KG, 3. HG, 4. DAG, 5. G, 6. DG, 7. CG, 8. MG): "))
                massak = float(
                    input("Masukkan Massanya(Hanya Angka, Contoh = 5): "))
                if massac == "1":
                    mas = massak * 1000
                elif massac == "2":
                    mas = massak
                elif massac == "3":
                    mas = massak / 10
                elif massac == "4":
                    mas = massak / 100
                elif massac == "5":
                    mas = massak / 1000
                elif massac == "6":
                    mas = massak / 10000
                elif massac == "7":
                    mas = massak / 100000
                elif massac == "8":
                    mas = massak / 1000000
                else:
                    print("Maaf Input Salah!")

                VeloMT = str(
                    input("Kecepatan Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while VeloMT not in velolist:
                    print("Satuan Yang Anda Masukkan Salah")
                    VeloMT = str(
                        input("Kecepatan Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                velo = float(
                    input("Masukkan Kecepatannya(Hanya Angka, Contoh = 15): "))
                if VeloMT == "1":
                    vel = velo * 1000
                elif VeloMT == "2":
                    vel = velo * 100
                elif VeloMT == "3":
                    vel = velo * 10
                elif VeloMT == "4":
                    vel = velo
                elif VeloMT == "5":
                    vel = velo / 10
                elif VeloMT == "6":
                    vel = velo / 100
                elif VeloMT == "7":
                    vel = velo / 1000
                else:
                    print("Maaf Input Salah!")
                disMT = str(input(
                    "Ketinggian Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                while disMT not in dislist:
                    print("Satuan Yang Anda Masukkan Salah")
                    disMT = str(input(
                        "Ketinggian Mu Dalam Satuan Apa? (1. KM, 2. HM, 3. DAM, 4. M, 5. DM, 6. CM, 7. MM): "))
                dis = float(
                    input("Masukkan Ketinggiannya(Hanya Angka, Contoh = 10): "))
                if disMT == "1":
                    hei = dis * 1000
                elif disMT == "2":
                    hei = dis * 100
                elif disMT == "3":
                    hei = dis * 10
                elif disMT == "4":
                    hei = dis
                elif disMT == "5":
                    hei = dis / 10
                elif disMT == "6":
                    hei = dis / 100
                elif disMT == "7":
                    hei = dis / 1000
                else:
                    print("Maaf Input Salah!")
                t4 = float(input("Masukkan Waktu Nya: "))
                Dek1 = (1/2 * massak * (vel ** 2))
                Dep1 = (massak * 10 * hei)
                Dem = (Dek1+Dep1) / t4
                print("Daya Nya Adalah: ", Dem, "Watt")
            else:
                print("Maaf Input Salah!")
        elif quest1 == "end":
            break
        else:
            print("Maaf Input Salah!")
    print("="*50)
    print("Physhics Calculator ENDED! By User")
    print("="*50)


def logout():
    set_user_authenticated(False)
    print("Logout successful.")


if __name__ == "__main__":
    main()
