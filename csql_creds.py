import os, sys

cred_file_name = "gcloud-stuff/application_default_credentials.json"

def main(args):
    print("Here is what is in the environment at startup time:")
    for name, value in os.environ.items():
        print("%s=%s" % (name, value))
    print("------------------------------------------------")
        # pull the relevant env vars for the items in the application_default_credentials.json file
    client_id     = os.getenv("GCLOUD_CLIENT_ID")
    client_secret = os.getenv("GCLOUD_CLIENT_SECRET")
    refresh_token = os.getenv("GCLOUD_REFRESH_TOKEN")
    user_type     = os.getenv("GCLOUD_USER_TYPE")

    # create a JSON like content with the actual cred values for the placeholders
    cred_content = """{
        "client_id": "%s",
        "client_secret": "%s",
        "refresh_token": "%s",
        "type": "%s"
    }\n""" % (client_id, client_secret, refresh_token, user_type)

    with open(cred_file_name, 'w') as f:
        f.write(cred_content)

if __name__ == "__main__":
    main(sys.argv[1:])