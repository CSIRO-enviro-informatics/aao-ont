from rdflib import Graph, Namespace, URIRef, Literal, RDF, XSD


def make_aaos():
    g = Graph()
    with open('AAOs.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(',')

            AAO = Namespace('http://test.linked.data.gov.au/def/aaos/')
            g.bind('aao', AAO)

            AAOS = Namespace('http://test.linked.data.gov.au/dataset/aaos/aao/')
            g.bind('aaos', AAOS)

            this_aao = URIRef(AAOS + words[0])

            if words[2] == 'Amendment':
                aao_class = URIRef('http://test.linked.data.gov.au/def/aaos/Amendment')
            else:
                aao_class = URIRef('http://test.linked.data.gov.au/def/aaos/AAO')

            g.add((
                this_aao,  # an AAO within the AAO register within the AAOs dataset
                RDF.type,  # an AAO is of type...
                aao_class  # of type AAO, as defined in the AAOs ontology
            ))

            DCT = Namespace('http://purl.org/dc/terms/')
            g.bind('dct', DCT)

            # the issued date of this AAO
            g.add((
                this_aao,
                DCT.issued,
                Literal(words[1], datatype=XSD.date)
            ))

    with open('aaos.ttl', 'w') as f:
        f.write(g.serialize(format='turtle').decode('utf-8'))


if __name__ == '__main__':
    make_aaos()
