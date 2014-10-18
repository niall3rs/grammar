#!/usr/bin/python

from nltk import *

def main():
  ugrammar = parse_fcfg("""
  S -> NP[AGR=?a] VP[AGR=?a, FORM=Pres] | Wh SQ | AP S
  SQ -> Verb[AGR=?a] NP[AGR=?a] VP[FORM=Inf]
  NP[AGR=?a] -> Verb[FORM=Gerund] NP[AGR=?a] | Det[AGR=?a] Nom[AGR=?a] | Nom[AGR=?a] | NP[AGR=?a] PP
  NP[AGR=[NUM=pl]] -> NP Conj NP
  Nom[AGR=?a] -> Adj Nom[AGR=?a] | ProperNoun[AGR=?a] | Noun[AGR=?a]
  VP[AGR=?a, FORM=Pres] -> Verb[AGR=?a, FORM=Pres, SUBCAT=Intrans] | Verb[AGR=?a, FORM=Pres, SUBCAT=Trans] NP | Verb[AGR=?a, FORM=Pres] S | Adv VP[AGR=?a, FORM=Pres]
  VP[FORM=Inf] -> Verb[FORM=Inf] NP
  PP -> Prep NP
  AP -> Aux S
  ProperNoun[AGR=[NUM=sg, PER=3]] -> 'Gromit' | 'Wallace' | 'Friday'
  Noun[AGR=[NUM=sg]] -> 'cheese' | 'kitchen'
  Verb[AGR=[NUM=sg, PER=3], FORM=Pres, SUBCAT=Trans] ->  'feeds' | 'eats' | 'does' | 'knows' | 'likes'
  Verb[AGR=[NUM=sg, PER=3], FORM=Pres, SUBCAT=Intrans] -> 'barks'
  Verb[FORM=Inf] -> 'eat' | 'like'
  Verb[AGR=[NUM=sg, PER=1], FORM=Pres] -> 'eat' | 'like'
  Verb[AGR=[NUM=pl], FORM=Pres] -> 'eat' | 'like'
  Verb[FORM=Gerund] -> 'eating'
  Det -> 'the'
  Conj -> 'and'
  Wh -> 'when'
  Adj -> 'tasty'
  Adv -> 'often'
  Prep -> 'in' | 'on'
  Aux -> 'when'
  """)
  
  uparser = FeatureChartParser(ugrammar)
  
  text = """\
  Gromit barks
  Wallace feeds Gromit
  Wallace and Gromit eat cheese
  when does Wallace eat cheese
  Wallace knows Gromit eats cheese
  Wallace likes eating cheese
  Gromit often eats tasty cheese in the kitchen on Friday
  when Gromit barks Wallace feeds Gromit
  Gromit eat cheese
  when does Gromit eats cheese
  Gromit barks Wallace"""
  
  sents = text.splitlines()
  
  for sent in sents:
    parses = uparser.nbest_parse(sent.split())
    print sent
    if len(parses) > 0:
      print len(parses), "parses:"
      for tree in parses:
        print tree, "\n"
    else:
      print "no parses\n"

if __name__ == '__main__':
  main()
