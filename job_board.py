class Job:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.applications = []

    def apply(self, applicant_name):
        self.applications.append(applicant_name)
        print(f"{applicant_name} has applied for the job: {self.title}")


class JobBoard:
    def __init__(self):
        self.jobs = []

    def add_job(self, title, description):
        job = Job(title, description)
        self.jobs.append(job)
        print(f"Job '{title}' added to the job board.")

    def list_jobs(self):
        if not self.jobs:
            print("No jobs available.")
            return
        print("Available Jobs:")
        for index, job in enumerate(self.jobs):
            print(f"{index + 1}. {job.title} - {job.description}")

    def apply_for_job(self, job_index, applicant_name):
        if 0 <= job_index < len(self.jobs):
            self.jobs[job_index].apply(applicant_name)
        else:
            print("Invalid job index.")


def main():
    job_board = JobBoard()

    while True:
        print("\nJob Board Menu:")
        print("1. Add Job")
        print("2. List Jobs")
        print("3. Apply for Job")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter job title: ")
            description = input("Enter job description: ")
            job_board.add_job(title, description)

        elif choice == '2':
            job_board.list_jobs()

        elif choice == '3':
            job_board.list_jobs()
            job_index = int(input("Enter the job number to apply for: ")) - 1
            applicant_name = input("Enter your name: ")
            job_board.apply_for_job(job_index, applicant_name)

        elif choice == '4':
            print("Exiting the job board.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
