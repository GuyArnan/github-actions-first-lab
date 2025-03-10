def main():
    print("--- GitHub Actions Runner Information ---")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Current Time: {datetime.datetime.now()}")
    print(f"Environment Variable GITHUB_ACTION: {os.getenv('GITHUB_ACTION')}")
    print(f"Environment Variable GITHUB_REPOSITORY: {os.getenv('GITHUB_REPOSITORY')}")
    print(f"Current Working Directory: {os.getcwd()}")
    print("--- End of Information ---")

if __name__ == "__main__":
    main()
