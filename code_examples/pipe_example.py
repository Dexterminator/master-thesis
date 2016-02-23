def worker(conn):
    conn.send("data")
    conn.close()

parent_conn, child_conn = multiprocessing.Pipe()
p = multiprocessing.Process(target=worker, args=(child_conn,))
p.start()
handle_data(parent_conn.recv())
p.join()
