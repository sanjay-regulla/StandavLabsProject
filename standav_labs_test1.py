from datetime import datetime
import pandas as pd

def validate_given_dates(start_date, end_date):
    

    try:
        start_date = datetime.strptime(start_date,'%Y%m%d')
        end_date = datetime.strptime(end_date,'%Y%m%d')

        start_year = start_date.year
        end_year = end_date.year
        
        if 1900<=int(start_year) and int(end_year)<=2100 and start_date < end_date:
            
            return start_date, end_date
    except :
        print ("Enter Proper date format")
            
 

         
def get_all_saturays(startdate,enddate):

    saturays_list  = pd.date_range(start=str(startdate), end=str(enddate+1),freq='W-SAT').strftime('%Y%m%d').tolist()
    
    return saturays_list


def get_saturday_of_every_month_between_start_end_dates(saturday_li,startdate,enddate) :

    
    saturday_in_months_dict = {}
    for dt in  saturday_li :
        
        year_month = dt[:6]
        if year_month in saturday_in_months_dict :
            saturday_in_months_dict[year_month].append(dt)
        else :
            saturday_in_months_dict[year_month] = [dt]


    sorted_saturday_in_months = sorted(saturday_in_months_dict.items(),key=lambda x:x[0])
    
    saturday_list = []
    for year_mnth,sat_li in sorted_saturday_in_months :
        
        for sat in sat_li :
            
            if startdate <= datetime.strptime(sat,'%Y%m%d') <= enddate  :
                saturday_date = int(sat[6:])
                if saturday_date%5 == 0  and sat_li.index(sat) !=3 :
                    saturday_list.append(sat)
                elif saturday_date%5 != 0  and sat_li.index(sat) ==3  :
                    saturday_list.append(sat)
                    
           
     
    return saturday_list
    
    


if __name__ == "__main__" :
    
    start_date = '20180728'
    end_date = '20180927'
    
    start_date, end_date = validate_given_dates(start_date, end_date)


    saturday_li = get_all_saturays(start_date.year,end_date.year)
    
    output_sat_list = get_saturday_of_every_month_between_start_end_dates(saturday_li,start_date,end_date)
    print ("The Output is:")
    for date in output_sat_list :
        print (date) 
    
