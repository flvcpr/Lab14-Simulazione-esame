from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getChrom():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select DISTINCT Chromosome 
                    from genes g 
                    where Chromosome >0"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["Chromosome"])
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select g.Chromosome as g1, g2.Chromosome as g2
                from interactions i ,genes g ,genes g2 
                where g.Chromosome!=g2.Chromosome 
                and g.Chromosome >0
                and g2.Chromosome >0
                and i.GeneID1 =g.GeneID
                and i.GeneID2 =g2.GeneID"""
        cursor.execute(query)
        for row in cursor:
            result.append((row["g1"],row["g2"]))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getPesi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select  distinct i.GeneID1 ,i.GeneID2, i.Expression_Corr , g.Chromosome as c1, g2.Chromosome as c2 
                    from interactions i ,genes g ,genes g2 
                    where g.Chromosome!=g2.Chromosome 
                    and g.Chromosome >0
                    and g2.Chromosome >0
                    and i.GeneID1 =g.GeneID
                    and i.GeneID2 =g2.GeneID
                    group by i.GeneID1 ,i.GeneID2 , g.Chromosome,g2.Chromosome
                    """
        cursor.execute(query)
        for row in cursor:
            result.append((row["c1"],row["c2"],row["Expression_Corr"]))
        cursor.close()
        conn.close()
        return result