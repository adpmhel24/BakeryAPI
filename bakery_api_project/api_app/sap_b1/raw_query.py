def it_query(docnum='', towhse=''):

    raw_query = f"""
        declare @docnum varchar(max)
        declare @towhse varchar(max)

        set @docnum = {"''" if not docnum else docnum};
        set @towhse = '{'' if not towhse else towhse }';

        SELECT*
        FROM [AKPOS].[dbo].vSAP_IT a1
        WHERE (a1.DocDate >= '20200910') and (a1.DocNum = @docnum or @docnum = '')
        and (a1.WhsCode = @towhse or @towhse = '') """
    return raw_query

# def po_query(docnum='', seriesname=''):
#     raw_query = f"""
#     DECLARE @docnum VARCHAR(20)
#     DECLARE @seriesname VARCHAR(30)
    
#     SET @docnum = {"''" if not docnum else docnum}
#     SET @seriesname = {"''" if not seriesname else seriesname}

#     SELECT
#     """