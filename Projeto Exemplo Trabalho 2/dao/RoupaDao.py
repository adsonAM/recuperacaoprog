from model.Roupa import Roupas


class RoupaDao:
    def __init__(self, connection):
        self.connection = connection

    def listarRoupa(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM roupa ORDER BY id'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            roupa = Roupas()
            roupa.id = item[0]
            roupa.marca = item[1]
            roupa.tamanho = item[2]
            roupa.tipo = item[3]

            lista.append(roupa)

        return lista

    def selecionarRoupa(self, id) -> Roupas:
        c = self.connection.cursor()
        c.execute(f"SELECT * FROM roupa WHERE id = {id}")
        recset = c.fetchone()
        c.close()

        print(recset)

        roupa = Roupas()
        roupa.id = recset[0]
        roupa.marca = recset[1]
        roupa.tamanho = recset[2]
        roupa.tipo = recset[3]

        return roupa

    def inserirRoupas(self, roupa:Roupas) ->Roupas:
        c = self.connection.cursor()
        c.execute("""
            insert into roupa(id, marca, tipo, tamanho)
            values('{}', '{}', '{}', '{}') RETURNING id
        """.format(roupa.id, roupa.marca, roupa.tamanho, roupa.tipo))

        self.connection.commit()

    def alterarRoupas(self, roupa: Roupas) -> Roupas:
        c = self.connection.cursor()
        c.execute("""
            update roupa
            SET marca = '{}', tamanho = '{}', tipo = '{}'
            WHERE id = '{}';
        """.format(roupa.marca, roupa.tamanho, roupa.tipo, roupa.id))

        self.connection.commit()

    def excluirRoupas(self, roupa: Roupas) -> Roupas:
        c = self.connection.cursor()
        c.execute("""
            delete from roupa
            where id = '{}'
        """.format(roupa.id))
        self.connection.commit()
