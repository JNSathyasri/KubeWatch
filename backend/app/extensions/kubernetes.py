from kubernetes import client

def get_core_api():
    return client.CoreV1Api()

def get_apps_api():
    return client.AppsV1Api()

def get_batch_api():
    return client.BatchV1Api()