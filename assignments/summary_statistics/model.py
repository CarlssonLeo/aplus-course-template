def summary_statistics(data):
    x_bar = sum(data)/len(data)
    std = ((sum([(x-x_bar)**2 for x in data])) / (len(data)-1))**0.5
    
    return {
        "mean": x_bar,
        "std": std,
        "min":  min(data),
        "max": max(data)
    }