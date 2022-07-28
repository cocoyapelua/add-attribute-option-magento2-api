import mysql.connector
import sshtunnel
import conf.constants as constants


def ssh_connect():
    global tunnel
    tunnel = sshtunnel.SSHTunnelForwarder(
        (constants.SSH_HOST, int(constants.SSH_PORT)),
        ssh_username=constants.SSH_USER,
        ssh_pkey=constants.KEY_FILE,
        remote_bind_address=(constants.SQL_HOSTNAME, int(constants.SQL_PORT)))

    tunnel.start()


def sql_connect():
    global conn
    conn = mysql.connector.connect(host=constants.SQL_HOST, user=constants.SQL_USERNAME,
                                   password=constants.SQL_PASSWORD, database=constants.SQL_DATABASE,
                                   port=tunnel.local_bind_port, use_pure=True)


def insert_query(query):
    data = conn.cursor(dictionary=True)
    data.execute(query)
    conn.commit()

    return data.lastrowid


def select_query(query):
    data = conn.cursor(dictionary=True)
    data.execute(query)

    return data.fetchall()


def sql_disconnect():
    conn.close()


def ssh_disconnect():
    tunnel.stop()
