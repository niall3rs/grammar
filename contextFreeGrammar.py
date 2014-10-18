#!/usr/bin/python

from nltk import *

def main():
  cfg = parse_cfg("""
  S -> NP VP | Wh SQ | AP S
  SQ -> Verb S
  NP -> NP Conj NP | Gerund NP | Det Nom | Nom | NP PP
  Nom -> Adj Nom | ProperNoun | Noun
  VP -> Verb | Verb NP | Verb S | Adv VP
  PP -> Prep NP
  AP -> Aux S
  ProperNoun -> 'Gromit' | 'Wallace' | 'Friday'
  Noun -> 'cheese' | 'kitchen'
  Verb -> 'barks' | 'feeds' | 'eat' | 'eats' | 'does' | 'knows' | 'like' | 'likes'
  Gerund -> 'eating'
  Det -> 'the'
  Conj -> 'and'
  Wh -> 'when'
  Adj -> 'tasty'
  Adv -> 'often'
  Prep -> 'in' | 'on'
  Aux -> 'when'
  """)
  
  cfparser = ChartParser(cfg)
  
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
    parses = cfparser.nbest_parse(sent.split())
    print sent
    if len(parses) > 0:
      print len(parses), "parses:"
      for tree in parses:
        print tree, "\n"
    else:
      print "no parses\n"

if __name__ == '__main__':
  main()
