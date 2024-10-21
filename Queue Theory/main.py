def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# Explanation of Kendal Models
print("******** Kendal Models 1/2/3/4/5 ********\n")
print("1 = {M, G}  ------> Packets Arrival Distribution")
print("2 = {M, G, D}  ---> Service Time Distribution")
print("3 = {1 .... N} ---> Number of serving people (like waiters)")
print("4 = {1 ... +oo} --> Number of clients/sources from where the load comes from")
print("5 = {1 ... +oo} --> Number of clients in the system (being served + waiting to be served)")



# 1. M/M/1 Model - Example with: lamda=2, mu=5
print("M/M/1 = 1 server, infinite external sources, infinite queue")
lamda = float(input("Give me arrival rate (lambda): "))
mu = float(input("Give me service rate (mu): "))
rho = lamda / mu
P0 = 1 - rho
print()

print(f"Traffic load = rho = lamda / mu = {rho:.2f}")
print(f"Probability of 0 clients in the system = P(0) = 1 - rho = {P0:.2f}")
print(f"Probability of n clients in the system = P(n) = P(0)*rho^n = {P0:.2f}*{rho:.2f}^n\n")

N = lamda / (mu - lamda)
Nq = rho**2 / (1 - rho)
Ns = N - Nq
print(f"Average number of clients (total)  in the system = N  = {N:.2f}")
print(f"Average number of clients (queue)  in the system = Nq = {Nq:.2f}")
print(f"Average number of clients (served) in the system = Ns = {Ns:.2f}\n")

T = 1 / (mu - lamda)
Ts = 1 / mu
Tq = T - Ts
print(f"Average total delay time in the system   = T = {T:.2f}")
print(f"Average time of service in the system    = Ts = {Ts:.2f}")
print(f"Average waiting time in the system queue = Tq = {Tq:.2f}\n")



# 2. M/M/1/oo/N - Example with: lamda=2, mu=5, N=3
def p(n, P0, rho):
    return P0 * rho**n

print("M/M/1/oo/N = 1 server, infinite external sources, finite queue")
lamda = float(input("Give me arrival rate (lambda): "))
mu = float(input("Give me service rate (mu): "))
N = int(input("Give me the number of total seats available (N): "))
rho = lamda / mu
P0 = (1 - rho) / 1 - rho**(N+1)
P_blockage = p(N, P0, rho)
print()

print(f"Traffic load = rho = lamda / mu = {rho:.2f}")
print(f"Probability of blockage = P(blockage) = P(N) = P({N}) = {100*P_blockage:.2f}%\n")
print(f"For 1 server and {N} total seats:\n")
for i in range(0, N + 1):
    print(f"P({i}) = {100*p(i, P0, rho):.2f}%")




# 3. M/M/N/oo/N (Erlang B) - Example with lamda=2, mu=1, N=5
def prob_erlang_b(n, N, rho):
    a = rho**n / factorial(n)
    b = sum([rho**i / factorial(i) for i in range(0, N + 1)])
    return a / b

print("M/M/N/oo/N = N servers, infinite external sources, N seats ---> no queue, non-zero blockage probability")
lamda = float(input("Give me arrival rate (lambda): "))
mu = float(input("Give me service rate (mu): "))
N = int(input("Give me the number of servers = number of total seats (N): "))
rho = lamda / mu
P_blockage = prob_erlang_b(N, N, rho)
print()

print(f"Traffic load = rho = lamda / mu = {rho:.2f}")
print(f"Probability of blockage = P(blockage) = P(N) = P({N}) = {100*P_blockage:.2f}%\n")
print(f"For rho={rho} and N={N} servers-total seats, we have: ")
for i in range(0, N + 1):
    print(f"P({i}) = {100*prob_erlang_b(i, N, rho):.2f}%")
print(f"P({N+1}) = P({N+2}) = .... = 0.00% (there is no queue)\n")

T_avg = 1 / mu
N_avg = rho * (1 - P_blockage)
print(f"Average waiting time in the system queue = T_avg = {T_avg:.2f}")
print(f"Average number of clients in the system  = N_avg = {N_avg:.2f}\n")
print("\n\n\n")





import matplotlib.pyplot as plt
print(f"Blockage probability: Searching for different values of N (not only for N={N})")
P_blockage_list = list()
N_list = list(range(1, 21))
for N in N_list:
    P_blockage_list.append(prob_erlang_b(N, N, rho))

d = {N_list[i] : f"{100*P_blockage_list[i]:.2f}%" for i in range(len(N_list))}
print(d, "\n\n")
plt.plot(N_list, P_blockage_list)
plt.plot(N_list, P_blockage_list, 'ro')
plt.grid(True)
plt.title(f"Blockage probability (rho={rho:.2f})")
plt.xlabel("Number of servers [N]")
plt.ylabel("Blockage probability [%]")
plt.show()



# 4. M/M/N/oo/oo (Erlang C) - Example with: lamda=6, mu=3, N=5
print("M/M/N/oo/oo = N servers, infinite external sources, infinite queue")
print("Rule: rho < 1 <----> lamda / mu*N < 1")
lamda = float(input("Give me arrival rate (lambda): "))
mu = float(input("Give me service rate (mu): "))
N = int(input("Give me the number of servers (N): "))
rho = lamda / mu
density_traffic_load = rho / N
print()

print(f"Traffic load = rho = lamda / mu = {rho:.2f}")
print(f"Density of traffic load = rho = lamda / mu = {density_traffic_load:.2f}")

P_blockage_erlang_B = prob_erlang_b(N, N, rho)
P_T = (N*P_blockage_erlang_B) / (N - rho*(1-P_blockage_erlang_B))
print(f"Probability of request delay = P_T = {100*P_T:.2f}%\n")

Nq = rho * P_T / (N - rho)
Ns = rho * N
N_sys = Nq + Ns
T_avg = 1 / mu + Nq / lamda
print(f"Average number of clients in the system =       N_sys = {N_sys:.2f}")
print(f"Average number of clients (queue)  in the system = Nq = {Nq:.2f}")
print(f"Average number of clients (served) in the system = Ns = {Ns:.2f}\n")
print(f"Average delay time in system = T_avg = {T_avg:.2f}")



# 5. M/M/N/M/N (Engset) - Example with: lamda=6, mu=3, N=5, M=10
def c(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print("M/M/N/M/N = N servers, M external sources, no queue")
lamda = float(input("Give me arrival rate (lambda): "))
mu = float(input("Give me service rate (mu): "))
N = int(input("Give me the number of servers-total seats (N): "))
M = int(input("Give me the number of external sources (M): "))
rho = lamda / mu
print()

print(f"Traffic load = rho = lamda / mu = {rho:.2f}")
print(f"Density of traffic load = rho = lamda / mu = {density_traffic_load:.2f}\n")

P_N = rho**N * c(M, N) / sum([rho**i * c(M, i) for i in range(0, N+1)])
P_L = rho**N * c(M-1, N) / sum([rho**i * c(M-1, i) for i in range(0, N+1)])
print(f"Probability of system congestion:   P_N = {100*P_N:.2f}%")
print(f"Probability of requests congestion: P_L = {100*P_L:.2f}%")
