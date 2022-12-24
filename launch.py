import argparse

from utils.inputDataUtils import *
from utils.stringOpUtils import *
from utils.terminalUtils import *
from utils.labelMakerUtils import *
from utils.solutionRoot import *

import y2022.d23.p1, y2022.d23.p2

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