import ast,pathlib
P=pathlib.Path(__file__).parents[1]/'contracts'/'contract.py';S=P.read_text(encoding='utf-8')
def gate():
 n=next(x for x in ast.parse(S).body if isinstance(x,ast.FunctionDef) and x.name=='waking_gate');z={};exec(compile(ast.Module([n],[]),str(P),'exec'),z);return z['waking_gate']
def test_surface():
 ast.parse(S)
 for x in ('bind_dream','wake','get_dream','get_dreams_page','run_nondet_unsafe'):assert x in S
def test_unavailable_witness_forfeits():assert gate()('RELEASED',3,3,True)=='FORFEITED'
def test_partial_evidence_lingers():assert gate()('RELEASED',2,3,False)=='LINGERING'
def test_every_term_must_be_proved():assert gate()('RELEASED',3,3,False)=='RELEASED'
def test_consensus_reads_frozen_terms_and_proofs():assert 'Frozen waking terms:' in S and 'Independent waking proofs:' in S
