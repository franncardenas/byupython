with open('hr_system.txt') as hr_system:
    
    for line in hr_system:
        #print(line)
        clean = line.strip()
        parts = line.split()
        
        name = parts[0]
        job = parts[2]
        salary = float(parts[3])/24
        id = parts[1]
        paycheck = 0
        if job.lower() == "engineer" :
            paycheck += 1000

        print(f"{name} (ID: {id}), {job} - ${salary + paycheck:.2f}")
        
