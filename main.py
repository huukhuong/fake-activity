import os
import datetime
from random import randrange

total_day = 1128  # total days back
commit_frequency = 3  # commit time per day
repo_link = "https://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@github.com/huukhuong/react-native"

tl = total_day  # time day
ctr = 1

now = datetime.datetime.now()

f = open("commit.txt", "w")

pointer = 0

while tl > 0:
    ct = commit_frequency
    while ct > 0:
        f = open("commit.txt", "a+")
        l_date = now + datetime.timedelta(days=-pointer)
        formatdate = l_date.strftime("%Y-%m-%d")
        random_number = randrange(0, 101)
        
        if random_number < 50 and random_number % 2 == 0:
            f.write(f"commit ke {ctr}: {formatdate}\n")
            f.close()
            os.system("git add .")
            os.system(f"git commit --date=\"{formatdate} 12:15:10\" -m \"commit ke {ctr}\"")
            print(f"commit ke {ctr}: {formatdate}")
            ctr += 1

        ct -= 1

    pointer += 1
    tl -= 1

os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")
