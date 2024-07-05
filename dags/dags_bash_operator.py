from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",    # Airflow 화면에서 보이는 dag 이름이다
                                    # dag 파일명과 dag_id는 가능한 일치시키는것이 좋다
    schedule="0 0 * * *",           # 매일 0시 0분에 돈다
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,            # 위에 설정한 시작일과 현재일 사이에 누락된 시간도 돌릴것인지, 아니면 안돌릴것인지 설정한다. 만약 true 설정시 누락된 시간을 전부 한번에 돌게 된다  
    dagrun_timeout=datetime.timedelta(minutes=60),
    # tags=["example", "example2"],              # 필요시 달아주면 된다
    # params={"example_key": "example_value"},   # 필요시 달아주면 된다
) as dag:
    bash_t1 = BashOperator(         # task 명이 된다
        task_id="bash_t1",          # task 명과 task_id는 같으면 좋다
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2    # 실행 순서