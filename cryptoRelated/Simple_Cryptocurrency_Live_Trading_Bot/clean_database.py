import os 
import pathlib
import sys

print('PYTHON PID:', os.getpid(), flush=True)
kill_cmd = '''taskkill /F /PID ''' + str(os.getpid())
print('EMERGENCY KILL COMMAND:', kill_cmd, flush=True)

if __name__=="__main__":
    coin = sys.argv[1]
    
    database_path = os.path.join(
        pathlib.Path(__file__).parent,
        os.path.join(
            "databases",
            f"{coin}stream.db"
        )
    )
    os.remove(database_path)