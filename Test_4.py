paragraph = 'That may be simply because colds are relatively mild, so the immune system doesn\'t mount a full-blown response, suggests Stanley Perlman, a pediatrician who studies immunology and microbiology at the University of Iowa. that\'s why people get colds over and over again," he says. it doesn\'t really tickle the immune response that much. he\'s studied one of the most severe coronaviruses, the one that causes SARS, and he\'s found that the degree of immunity depended on the severity of the disease. sicker people remained immune for much longer, in some cases many years. for most people exposed to the novel coronavirus, "I think in the short term you\'re going to get some protection," Perlman says. it\'s really the time of the protection that matters'

def capitalize( paragraph ):
	output = ''
	p = 0
	while p < len( paragraph ):
		if paragraph[p] == '.':
			output = output + '. ' + paragraph[p + 2].upper()
			p = p + 2
		elif p == 0:
			output = output + paragraph[p].upper()
		else:
			output = output + paragraph[p].lower()
		p = p + 1
	return output


print( capitalize( paragraph ) )