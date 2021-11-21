import pathlib
import os
import subprocess

def prepare_lines(data):
    lines = []
    for coin in data:
        lines.append(f"""set VAR_1={coin}\n""")
        lines.append(f"""set VAR_2={data[coin]["entry"]}\n""")
        lines.append(f"""set VAR_3={data[coin]["lookback_in_sec"]}\n""")
        lines.append(f"""set VAR_4={data[coin]["quantity"]}\n""")
        lines.append(f"""start python populate_database.py %1 %VAR_1%\n""")
        lines.append(f"""start python trade.py %1 %VAR_1% %VAR_2% %VAR_3% %VAR_4%\n""")
    return lines


if __name__=="__main__":
    data = {
        "BTCUSDT": {
            "entry" : 0.001,
            "lookback_in_sec" : 60,
            "quantity" : 0.001 
        },
        "ETHUSDT": {
            "entry" : 0.001,
            "lookback_in_sec" : 60,
            "quantity" : 0.001 
        }
    }
    lines = prepare_lines(data)
    current_directory = str(pathlib.Path(__file__).parent.resolve())

    with open("start.bat","w") as bat:
        bat.writelines(
           lines
        )
        
    subprocess.call([f"{os.path.join(current_directory,'start.bat')}"])

    os.remove(os.path.join(current_directory,'start.bat'))