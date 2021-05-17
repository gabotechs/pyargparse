from awesome_args import Arguments


class Args(Arguments):
    db_host: str
    db_user: str = "cassandra"
    db_port: int = 5000


args = Args()
print(args)
