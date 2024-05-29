import synapseclient
import synapseutils

# Initialize Synapse client
syn = synapseclient.Synapse()

# Login to Synapse with your authentication token
syn.login(authToken="eyJ0eXAiOiJKV1QiLCJraWQiOiJXN05OOldMSlQ6SjVSSzpMN1RMOlQ3TDc6M1ZYNjpKRU9VOjY0NFI6VTNJWDo1S1oyOjdaQ0s6RlBUSCIsImFsZyI6IlJTMjU2In0.eyJhY2Nlc3MiOnsic2NvcGUiOlsidmlldyIsImRvd25sb2FkIiwibW9kaWZ5Il0sIm9pZGNfY2xhaW1zIjp7fX0sInRva2VuX3R5cGUiOiJQRVJTT05BTF9BQ0NFU1NfVE9LRU4iLCJpc3MiOiJodHRwczovL3JlcG8tcHJvZC5wcm9kLnNhZ2ViYXNlLm9yZy9hdXRoL3YxIiwiYXVkIjoiMCIsIm5iZiI6MTcxNjc4ODA2NCwiaWF0IjoxNzE2Nzg4MDY0LCJqdGkiOiI4Mzk4Iiwic3ViIjoiMzUwNDQ1NCJ9.ODu0tcx3dLt1d1Xiavyr7WGaKTnhO9_OblxPSYV9KyrrOmDWyumqrJmG2FurHKnzdWIcA2GY9Lu5QKN-z_2R5F0WXJsiGDe-jW9pPqYfd99FTDO1hdL5sAoe46mMLdwNPOiXRDC7SGa-2EJKZ_HKZKbn1e4uGD1g-w4UmPn5cOz7hyQKav7Wjy3oQpKIIVZIHCJmEJLdXNTs7oJGIYVNMF3Dg-N1YsVzLBVIqWj5jMPgPju5_ptVPd3uokFbtvwkOMHXvr7aRFOIhkYS2WUCVqWGjw7idGfSu3jAopGY7gyMD1rREfVpyKF_Qu46Torcd5z_j2Z3yphw8XJlFxwsHA")

# Specify the Synapse ID of the dataset
dataset_id = 'syn3193805'

# Download the dataset to the specified directory
files = synapseutils.syncFromSynapse(syn, dataset_id, path='data/Synapse')