from datetime import datetime
from binary_search_tree import BinarySearchTree


def read(reader, job_cache):
    for record in reader:
        job_cache.insert(record)

def load_jobs(job_cache):
    default_jobs_list = "jobs.txt"
    custom_jobs_list = "custom_jobs.txt"

    try:
        with open(custom_jobs_list, "r") as reader:
            print("\nLoading custom job Schedule")
            read(reader, job_cache)
    except FileNotFoundError:
        try:
            with open(default_jobs_list, "r") as reader:
                print("\nLoading default job Schedule")
                read(reader, job_cache)
        except FileNotFoundError:
            print("\n !!! File Not Found, continuing with no Scheduled jobs !!! \n")


def print_menu():
    print("")
    print("Commands: ")
    print("[ 1 ] to list jobs")
    print("[ 2 ] to insert job")
    print("[ 3 ] to remove job")
    print("[ 4 ] to exit")
    print("")

def list_jobs(job_cache):
    job_cache.in_order()

def get_job_details():
    try:
        job_title = str(input("please enter the jobs title: "))
    except ValueError:
        raise ValueError("\n !!! invalid job title !!!")

    try:
        time_format = "%H:%M:%S"
        start_time = input("please enter the jobs start time (HH:MM:SS): ")
        datetime.strptime(start_time, time_format)
    except ValueError:
        raise ValueError("\n !!! invalid time format !!!")

    try:
        duration = int(input("please enter the jobs duration (minutes): "))
    except ValueError:
        raise ValueError("\n !!! invalid job duration !!!")

    return str(start_time) + "," + str(duration) + "," + job_title

def insert_job(job_cache):
    try:
        job_cache.insert(get_job_details())
        job_cache.write_to_file()
    except ValueError as error:
        print(error)

def remove_job(job_cache):
    try:
        start_time, duration, job_title = get_job_details().split(",")
        start_time = datetime.strptime(start_time, '%H:%M:%S').time()
        job_to_remove = job_cache.find_value(start_time)
        print(job_to_remove)
        if job_to_remove.start_time == start_time and job_to_remove.duration == duration and job_to_remove.job_title == job_title:
            job_cache.delete_value(start_time)
            job_cache.write_to_file()
        else:
            raise ValueError("\n !!! job title, start time and duration must match entry exactly !!!")
    except ValueError as error:
        print(error)

def exit():
    quit()

def job_scheduler():
    job_cache = BinarySearchTree()
    load_jobs(job_cache)
    while(True):
        print_menu()
        try:
            command = int(input("please enter a command: "))
            print("")
            if command < 1 or command > 4:
                raise ValueError()
            elif command == 1:
                list_jobs(job_cache)
            elif command == 2:
                insert_job(job_cache)
            elif command == 3:
                remove_job(job_cache)
            elif command == 4:
                exit()
        except ValueError:
            print("\n !!! invalid command !!! \n")

job_scheduler()
