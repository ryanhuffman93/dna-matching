from sys import argv, exit
import pandas

if len(argv) != 3: #if there are not 3 command line aruments
    print("please specify a database and text file") #give user an error message
    exit(1) #quit running the program

suspects = pandas.read_csv(argv[1]) #open the csv file in the 2nd command line argument to a database called 'suspects'.

evidence = list() #initalize a list of evidence to be used to later keep track of the max streaks for each dna strand
verdicts = list() #initalize a list of verdicts for each suspect to later keep track of if we have any guilty veridicts amoung our suspects
rows = len(suspects) #define rows as the number of rows in our suspect data
columns = len(suspects.columns) #define columns as the number of columns in our suspect data

### ANALYZING THE EVIDENCE
for j in suspects.columns: #check through the evidence for the header of each column (dna strand) in the suspect data
    if j != "name": #allows program to avoid initializing the first item in our evidence list to 0 when checking the text for 'name'
        text = open(argv[2], "r") #open the text file with the dna data to investigate
        string = text.read() #call the text in that file 'string'
        length = len(string) #define the length of the text in the file as 'length'

        streak = 0 #set starting streak value to zero
        count = 0 #set starting count value to zero
        i = 0 #set starting i value to zero. Will use to iterate through the text.

        while(i < length): #iterate through the text file
            if string[i:i+(len(j))] == j: #does this string of characters match the dna strand?
                count += 1 #if it does, add one to the count
                i += (len(j)) #jump to the following space after the string to check the next string
                if count > streak: #if the count is greater than the max streak
                    streak = count #then set the max streak to this count
            else: #if the string doesn't match the dna strand
                count = 0 #reset the count to zero (so that the count isn't cumulative)
                i+=1 #move to the next character in the text
        evidence.append(streak) #add the longest streak of this dna strand to the evidence list
#print(evidence) #in case you'd like to see the list of evidence

### COMPARING THE EVIDENCE VS THE SUSPECTS
for i in range(rows): #check each suspect by iterating through the csv rows
    j = 1 #initialize j to 1 to iterate through the suspect data while ignoring names
    k = 0 #initialize k to 0 to compare against the evidence list starting at the first strand
    while j < columns: #check each dna strand until you get to the end of the list
        if (suspects.iloc[i,j] == evidence[k]) and (j == (columns - 1)): #if there's a dna match and you've checked all the strands
            print(f"{suspects.iloc[i,0]} is guilty") #say that person is guilty
            verdicts.append("guilty") #add a guilty charge to the verdict results list for that suspect
            break #move on to the next suspect
        elif suspects.iloc[i,j] == evidence[k]: #if there's a dna match but you haven't checked all of the strands
            j += 1 #move to the next space in the suspects file
            k += 1 #move to the next space in the evidence list
        else: #there is no dna match
            verdicts.append("innocent") #add innocent to the verdict results for that suspect
            break #move on to the next suspect

if "guilty" not in verdicts: #check the verdict results to see if no one was found guilty
    print("No match") #say that there were no dna matches