import argparse

from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

# import y2015.d11.p1,y2015.d11.p2 
# import y2015.d01.p1,y2015.d01.p2,y2015.d02.p1,y2015.d02.p2,y2015.d03.p1,y2015.d03.p2,y2015.d04.p1,y2015.d04.p2,y2015.d05.p1,y2015.d05.p2
# import y2015.d06.p1,y2015.d06.p2,y2015.d07.p1,y2015.d07.p2,y2015.d08.p1,y2015.d08.p2,y2015.d09.p1,y2015.d09.p2,y2015.d10.p1,y2015.d10.p2
# import y2015.d12.p1,y2015.d12.p2 

# import y2016.d11.p1,y2016.d11.p2 
# import y2016.d01.p1,y2016.d01.p2,y2016.d02.p1,y2016.d02.p2,y2016.d03.p1,y2016.d03.p2,y2016.d04.p1,y2016.d04.p2,y2016.d05.p1,y2016.d05.p2
# import y2016.d06.p1,y2016.d06.p2,y2016.d07.p1,y2016.d07.p2,y2016.d08.p1,y2016.d08.p2,y2016.d09.p1,y2016.d09.p2,y2016.d10.p1,y2016.d10.p2

# import y2017.d01.p1,y2017.d01.p2,y2017.d02.p1,y2017.d02.p2,y2017.d03.p1,y2017.d03.p2,y2017.d04.p1,y2017.d04.p2,y2017.d05.p1,y2017.d05.p2
# import y2017.d06.p1,y2017.d06.p2,y2017.d07.p1,y2017.d07.p2,y2017.d08.p1,y2017.d08.p2,y2017.d09.p1,y2017.d09.p2,y2017.d10.p1,y2017.d10.p2
# import y2017.d11.p1, y2017.d11.p2 
# import y2017.d12.p1, y2017.d12.p2 

# import y2018.d01.p1,y2018.d01.p2,y2018.d02.p1,y2018.d02.p2,y2018.d03.p1,y2018.d03.p2,y2018.d04.p1,y2018.d04.p2,y2018.d05.p1,y2018.d05.p2
# import y2018.d06.p1,y2018.d06.p2,y2018.d07.p1,y2018.d07.p2,y2018.d08.p1,y2018.d08.p2,y2018.d09.p1,y2018.d10.p1,y2018.d10.p2
# import y2018.d11.p1,y2018.d11.p2
# import y2018.d12.p1,y2018.d12.p2

# import y2019.d01.p1,y2019.d01.p2,y2019.d02.p1,y2019.d02.p2,y2019.d03.p1,y2019.d03.p2,y2019.d04.p1,y2019.d04.p2,y2019.d05.p1,y2019.d05.p2
# import y2019.d06.p1,y2019.d06.p2,y2019.d07.p1,y2019.d07.p2,y2019.d08.p1,y2019.d08.p2,y2019.d09.p1,y2019.d09.p2,y2019.d10.p1,y2019.d10.p2
# import y2019.d11.p1,y2019.d11.p2
# import y2019.d12.p1,y2019.d12.p2

# import y2020.d01.p1,y2020.d01.p2,y2020.d02.p1,y2020.d02.p2,y2020.d03.p1,y2020.d03.p2,y2020.d04.p1,y2020.d04.p2,y2020.d05.p1,y2020.d05.p2
# import y2020.d06.p1,y2020.d06.p2,y2020.d07.p1,y2020.d07.p2,y2020.d08.p1,y2020.d08.p2,y2020.d09.p1,y2020.d09.p2,y2020.d10.p1,y2020.d10.p2
# import y2020.d11.p1,y2020.d11.p2
# import y2020.d12.p1,y2020.d12.p2

# import y2021.d01.p1,y2021.d01.p2,y2021.d02.p1,y2021.d02.p2,y2021.d03.p1,y2021.d03.p2,y2021.d04.p1,y2021.d04.p2,y2021.d05.p1,y2021.d05.p2
# import y2021.d06.p1,y2021.d06.p2,y2021.d07.p1,y2021.d07.p2,y2021.d08.p1,y2021.d08.p2,y2021.d09.p1,y2021.d09.p2,y2021.d10.p1,y2021.d10.p2
# import y2021.d11.p1,y2021.d11.p2,y2021.d12.p1,y2021.d12.p2,y2021.d13.p1,y2021.d13.p2,y2021.d14.p1,y2021.d14.p2,y2021.d15.p1,y2021.d15.p2
# import y2021.d16.p1,y2021.d16.p2,y2021.d17.p1,y2021.d17.p2,y2021.d18.p1,y2021.d18.p2,y2021.d19.p1,y2021.d19.p2,y2021.d20.p1,y2021.d20.p2
# import y2021.d21.p1,y2021.d21.p2,y2021.d22.p1,y2021.d22.p2,y2021.d23.p1,y2021.d23.p2,y2021.d24.p1,y2021.d24.p2,y2021.d25.p1,y2021.d25.p2

# import y2022.d01.p1, y2022.d01.p2
# import y2022.d02.p1, y2022.d02.p2
# import y2022.d03.p1, y2022.d03.p2
# import y2022.d04.p1, y2022.d04.p2
# import y2022.d05.p1, y2022.d05.p2
# import y2022.d06.p1, y2022.d06.p2
# import y2022.d07.p1, y2022.d07.p2
# import y2022.d08.p1, y2022.d08.p2
# import y2022.d09.p1, y2022.d09.p2
# import y2022.d10.p1, y2022.d10.p2
# import y2022.d11.p1, y2022.d11.p2
# import y2022.d12.p1, y2022.d12.p2
# import y2022.d13.p1, y2022.d13.p2
# import y2022.d14.p1, y2022.d14.p2
# import y2022.d15.p1, y2022.d15.p2
import y2022.d17.p1, y2022.d17.p2

END_YEAR=2022

def runDay(label, inputFile, logic):
    startMs = time.time()
    result = logic(inputFile)
    elapsedMs = round((time.time() - startMs)*1000)
    
    return (label, result[0], formatElapsedMsHuman(elapsedMs), 0 if result[0] == result[1] else 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", required=False, type=int)
    parser.add_argument("--day", required=False, type=int)
    parser.add_argument("--part", required=False, type=int)

    args = parser.parse_args()

    if args.year and args.day and args.part:
        yearLabel = "y%d"%args.year
        dayLabel = "d{:02d}".format(args.day) 
        partLabel = "p%d"%args.part

        runSolution(getattr(getattr(globals()[yearLabel], dayLabel), partLabel).solution, "./%s/%s/input.txt" % (yearLabel, dayLabel))
    else:
        years = [args.year] if args.year else [y for y in range(2015,END_YEAR+1)]
        days = [args.day] if args.day else [d for d in range(1,26)]
        parts = [args.part] if args.part else [1,2]

        results = []
        for year in years:
            for day in days:
                for part in parts:
                    yearLabel = "y%d"%year
                    dayLabel = "d{:02d}".format(day) 
                    partLabel = "p%d"%part

                    completeLabel = '%s/%s/%s' % (yearLabel, dayLabel, partLabel)

                    try:
                        logic = getattr(getattr(globals()[yearLabel], dayLabel), partLabel).solution
                        inputFile = "./%s/%s/input.txt" % (yearLabel, dayLabel)

                        results.append(runDay(completeLabel, inputFile, logic))
                    except AttributeError:
                        # log(red("ERROR", completeLabel))
                        results.append((completeLabel, 'n/a', '               n/a', 3))
                    except:
                        # log(red("ERROR", completeLabel))
                        results.append((completeLabel, 'n/a', '               n/a', 2))

                    log(dark("Finished", completeLabel))

        statusLabels = [green('   OK  '), yellow(' CHECK '), red(' ERROR '), dark('MISSING')]

        log(light(" STATUS |    PUZZLE    |               TIME | RESULT"))
        for result in results:
            log(statusLabels[result[-1]], '|', result[0],'|', result[2], '|', result[1],)