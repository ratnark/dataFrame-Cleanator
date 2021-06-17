import pandas as pd
df = pd.read_excel('C:\\Users\\1787912\\Desktop\\rationalisation\\Migration_Artifacts_Repository.xlsx',
                   sheet_name="Sheet2")  
df = df.fillna('NAREMOVE')

reportNameList = ['China_Cash',
'Collections Raw Data',
'Daily_CMM_Webcash_Recon',
'Daily_COH_Operational',
'Dispositions_Controls_Dashboard',
'FTRN Raw Data',
'FX_Cashpool_Adjustments',
'CC_Funding_Landscape',
'LE_Funding_Landscape',
'Liquidity_OwnerShip',
'mySheets_Payment_Viewer',
'Regional_Cash',
'TRAX_Payment_Monitoring',
'Webcash Transactional Data - Self Service Tool'
]

#df[~df.C.str.contains("XYZ")]

def returnFunc(reportName):
    cv = 'Consumption View'
    bv = 'Base View'
    so = 'CDL Source Object'
    
    report_name = df.loc[df['Report Name'] == reportName]
    
    removedDuplicateConsumptionView = pd.DataFrame({'dcol': report_name[cv].unique()})
    removedDuplicateBaseView = pd.DataFrame({'dcol': report_name[bv].unique()})  
    
    x = removedDuplicateConsumptionView.append(removedDuplicateBaseView)
    x = x.drop_duplicates()
    x = x[~x['dcol'].isin(['NAREMOVE','Subtotal','(Empty)'])]
    x = x[~x.dcol.str.contains('_il_')]
    denodoView = x[~x.dcol.str.contains('_icf_')]
    denodoView["reportName"] = reportName

    # print(denodoView, len(denodoView))
    removedDuplicateSObject = pd.DataFrame({'ccol': report_name[so].unique()})  
    y = removedDuplicateSObject.drop_duplicates()
    y = y[~y['ccol'].isin(['NAREMOVE','Subtotal','(Empty)'])]
    y = y[~y.ccol.str.contains('_il_')]
    y = y[~y.ccol.str.contains('_icf_')]
    cdlView = y[~y.ccol.str.contains('_cdh_')]
    cdlView["reportName"] = reportName
    # print(y, len(y))
    return [denodoView,cdlView]

outputChina_Cash = returnFunc('China_Cash')
outputCollections_Raw_Data = returnFunc('Collections Raw Data')
outputDaily_CMM_Webcash_Recon = returnFunc('Daily_CMM_Webcash_Recon')
outputDaily_COH_Operational = returnFunc('Daily_COH_Operational')
outputDispositions_Controls_Dashboard = returnFunc('Dispositions_Controls_Dashboard')
outputFTRN_Raw_Data = returnFunc('FTRN Raw Data')
outputFX_Cashpool_Adjustments = returnFunc('FX_Cashpool_Adjustments')
outputCC_Funding_Landscape = returnFunc('CC_Funding_Landscape')
outputLE_Funding_Landscape = returnFunc('LE_Funding_Landscape')
outputLiquidity_OwnerShip = returnFunc('Liquidity_OwnerShip')
outputmySheets_Payment_Viewer = returnFunc('mySheets_Payment_Viewer')
outputRegional_Cash = returnFunc('Regional_Cash')
outputRegional_CashTRAX_Payment_Monitoring = returnFunc('TRAX_Payment_Monitoring')
outputWebcash_Transactional_Data = returnFunc('Webcash Transactional Data - Self Service Tool')


finalDenodoView = pd.concat([outputChina_Cash[0],outputCollections_Raw_Data[0],
                                outputDaily_CMM_Webcash_Recon[0],outputDaily_COH_Operational[0],
                                outputDispositions_Controls_Dashboard[0],outputFTRN_Raw_Data[0],
                                outputFX_Cashpool_Adjustments[0],outputCC_Funding_Landscape[0],
                                outputLE_Funding_Landscape[0],outputLiquidity_OwnerShip[0],
                                outputmySheets_Payment_Viewer[0],outputRegional_Cash[0],
                                outputRegional_CashTRAX_Payment_Monitoring[0],
                                outputWebcash_Transactional_Data[0]])
finalCDLSource = pd.concat([outputChina_Cash[1],outputCollections_Raw_Data[1],
                                outputDaily_CMM_Webcash_Recon[1],outputDaily_COH_Operational[1],
                                outputDispositions_Controls_Dashboard[1],outputFTRN_Raw_Data[1],
                                outputFX_Cashpool_Adjustments[1],outputCC_Funding_Landscape[1],
                                outputLE_Funding_Landscape[1],outputLiquidity_OwnerShip[1],
                                outputmySheets_Payment_Viewer[1],outputRegional_Cash[1],
                                outputRegional_CashTRAX_Payment_Monitoring[1],
                                outputWebcash_Transactional_Data[1]])


finalDenodoView.to_csv('C:\\Users\\1787912\\Desktop\\rationalisation\\denodoView.csv',index=False, mode='a', header=False)

finalCDLSource.to_csv('C:\\Users\\1787912\\Desktop\\rationalisation\\cdlScource.csv', index=False,mode='a', header=False)
