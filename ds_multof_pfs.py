def ds_multof_pfs(nMin, nMax):
    result = []
    
    for n in range(nMin, nMax + 1):
        # Find the prime factors and sum them
        pfs = 0
        temp = n
        for i in range(2, int(n ** 0.5) + 1):
            while temp % i == 0:
                pfs += i
                temp //= i
        if temp > 1:
            pfs += temp
        
        # Find the divisors and sum them
        ds = 1 + n  # 1 and n itself are always divisors
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                ds += i
                if i != n // i:
                    ds += n // i
        
        # Check the property
        if pfs and ds % pfs == 0:
            result.append(n)
    
    return result

print(ds_multof_pfs(10, 100))
# Output: [12, 15, 35, 42, 60, 63, 66, 68, 84, 90, 95]

print(ds_multof_pfs(20, 120))
# Output: [35, 42, 60, 63, 66, 68, 84, 90, 95, 110, 114, 119]
