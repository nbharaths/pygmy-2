import numpy as np

client_search_time = np.loadtxt('./times/client_search_time.txt')
frontend_search_time = np.loadtxt('./times/frontend_search_time.txt')
catalog_search_time = np.loadtxt('./times/catalog_search_time.txt')

mean_client_search_time = np.mean(client_search_time)
mean_frontend_search_time = np.mean(frontend_search_time)
mean_catalog_search_time = np.mean(catalog_search_time)

print(mean_client_search_time, mean_frontend_search_time, mean_catalog_search_time)

client_lookup_time = np.loadtxt('./times/client_lookup_time.txt')
frontend_lookup_time = np.loadtxt('./times/frontend_lookup_time.txt')
catalog_lookup_time = np.loadtxt('./times/catalog_lookup_time.txt')

mean_client_lookup_time = np.mean(client_lookup_time)
mean_frontend_lookup_time = np.mean(frontend_lookup_time)
mean_catalog_lookup_time = np.mean(catalog_lookup_time)

print(mean_client_lookup_time, mean_frontend_lookup_time, mean_catalog_lookup_time)

client_buy_time = np.loadtxt('./times/client_buy_time.txt')
frontend_buy_time = np.loadtxt('./times/frontend_buy_time.txt')
order_buy_time = np.loadtxt('./times/order_buy_time.txt')
catalog_buy_time = np.loadtxt('./times/catalog_buy_time.txt')

mean_client_buy_time = np.mean(client_buy_time)
mean_frontend_buy_time = np.mean(frontend_buy_time)
mean_order_buy_time = np.mean(order_buy_time)
mean_catalog_buy_time = np.mean(catalog_buy_time)

print(mean_client_buy_time, mean_frontend_buy_time, mean_order_buy_time, mean_catalog_buy_time)
