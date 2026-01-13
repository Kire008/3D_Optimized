import os
import datetime

class Log:
    def __init__(self):
        # Logs path
        self.logs_path = os.path.join("Log/logs/")
        num_logs = len(os.listdir(self.logs_path))

        # Create log
        self.log_name = f"log_{datetime.datetime.now().strftime("%d_%m_%Y-%H_%M_%S")}.txt"
        self.current_log = os.path.join(f"{self.logs_path}{self.log_name}")

        with open(self.current_log, "w") as f:
            f.write(f"Created {self.log_name}\n")



    def log(self, info):
        with open(self.current_log, 'a') as f:
            f.write(info)

    def clear_all_logs(self):
        for log in os.listdir(self.logs_path):
            if log != self.log_name:
                os.remove(f"{self.logs_path}/{log}")



if __name__ == "__main__":
    log = Log()
    log.clear_all_logs()