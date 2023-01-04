from hashlib import sha1
from multiprocessing import Process

def hash_script(a, b, i):
    f = open("old-03" + "_" + str(i) + ".txt", 'w')
    result = ""
    for i in range(a, b):
        result = str(i) + "salt_for_you"
        for j in range(0, 500):
            result = sha1(result.encode('utf-8'))
            result = result.hexdigest()
        f.write(str(i) + " > " + result + '\n')
    f.close()
    return

if __name__ == '__main__':
    p1 = Process(target=hash_script, args=(10000000, 20000000, 1))
    p2 = Process(target=hash_script, args=(20000000, 30000000, 2))
    p3 = Process(target=hash_script, args=(30000000, 40000000, 3))
    p4 = Process(target=hash_script, args=(40000000, 50000000, 4))
    p5 = Process(target=hash_script, args=(50000000, 60000000, 5))
    p6 = Process(target=hash_script, args=(60000000, 70000000, 6))
    p7 = Process(target=hash_script, args=(70000000, 80000000, 7))
    p8 = Process(target=hash_script, args=(80000000, 90000000, 8))
    p9 = Process(target=hash_script, args=(90000000, 100000000, 9))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()