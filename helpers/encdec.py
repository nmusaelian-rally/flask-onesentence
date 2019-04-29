import os
from google.cloud import kms_v1
from google.cloud.kms_v1 import enums

PROJECT_ID   = os.getenv('PROJECT_ID')
LOCATION_ID  = os.getenv('LOCATION_ID')
KEY_RING_ID  = os.getenv('KEY_RING_ID')
CRYPTOKEY_ID = os.getenv('CRYPTOKEY_ID')

def encrypt_symmetric(project_id, location_id, key_ring_id, crypto_key_id,
                      plaintext):
    """Encrypts input plaintext data using the provided symmetric CryptoKey."""

    # Creates an API client for the KMS API.
    client = kms_v1.KeyManagementServiceClient()

    # The resource name of the CryptoKey.
    name = client.crypto_key_path_path(project_id, location_id, key_ring_id,
                                       crypto_key_id)

    # Use the KMS API to encrypt the data.
    response = client.encrypt(name, plaintext)
    return response.ciphertext


def decrypt_symmetric(project_id, location_id, key_ring_id, crypto_key_id,
                      ciphertext):
    """Decrypts input ciphertext using the provided symmetric CryptoKey."""

    # Creates an API client for the KMS API.
    client = kms_v1.KeyManagementServiceClient()

    # The resource name of the CryptoKey.
    name = client.crypto_key_path_path(project_id, location_id, key_ring_id,
                                       crypto_key_id)
    # Use the KMS API to decrypt the data.
    response = client.decrypt(name, ciphertext)
    return response.plaintext