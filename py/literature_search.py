"""Demo: text mining projects."""

import time

import webbrowser

from lisc.count import Count
from lisc.scrape import scrape_counts

###################################################################################################
###################################################################################################

def main():

    print("\nAUTOMATED LITERATURE SEARCH\n")

    input('\n>> Press to see terms\n')

    terms_brain = [['theta oscillation'], ['beta oscillation']]
    terms_behav = [['memory'], ['motor']]

    print('BRAIN TERMS')
    for term in terms_brain:
        print('\t' + term[0])

    print('BEHAV TERMS')
    for term in terms_behav:
        print('\t' + term[0])

    input('\n>> Press to run scrape\n')

    # Initialize counts object
    counts = Count()
    counts.set_terms(terms_brain, 'A')
    counts.set_terms(terms_behav, 'B')
    counts.run_scrape(verbose=True)

    input('\n>> Press to see results\n')

    # Check the highest associations for each term
    counts.check_cooc('A')

    # Jump over to ERP-SCANR site
    input('\n>> Press to jump to project site\n')
    print("Opening ERP-SCANNER WebSite")
    webbrowser.get('Safari').open('http://tomdonoghue.github.io/ERP_SCANR/')


if __name__ == "__main__":
    main()
