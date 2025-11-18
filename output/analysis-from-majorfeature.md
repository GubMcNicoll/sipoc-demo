# Analysis from majorfeature rules

This report classifies work items as major/minor/uncertain using heuristics derived from `instructions/majorfeature.md`.

## Summary

- Total rows analysed: 1111
- Predicted major: 936
- Predicted minor: 56
- Predicted uncertain: 119

## Keyword matches (top 30)

- `add` : 666
- `new` : 530
- `support` : 344
- `default` : 192
- `regulatory` : 156
- `validation` : 155
- `enable` : 147
- `compliance` : 120
- `\bcompliance\b` : 109
- `enhance` : 95
- `fix` : 92
- `tax` : 91
- `mapping` : 85
- `\bminor\b` : 84
- `minor` : 84
- `\bmapping\b` : 79
- `\blogs\b` : 63
- `schema` : 49
- `convert` : 47
- `R3` : 43
- `improve` : 40
- `rename` : 38
- `caption` : 37
- `\brename\b` : 32
- `performance` : 30
- `e-?invoice` : 25
- `R2` : 24
- `\bICS2\b` : 23
- `ICS2` : 23
- `\bComplianceWise\b` : 22

## Mismatches vs CSV Classification

- Total mismatches: 197

| WorkItem | Summary | CSV Classification | Predicted | Matched patterns |
|---|---|---:|---|---|
| WI00904060 | Total Allocation Statistics Section UI Enhancements | minor | major | support |
| WI00887209 | Turn off Audit Events for Declaration tables | minor | major | add, enable, support |
| WI00865431 | GCT Turn AUX WhiteList into BlackList | minor | major | new, add, support |
| WI00841200 | [S2S] Customer Integrated Applications Documentation | minor | uncertain |  |
| WI00901513 | Registries, messages and hint adjustments for reopen period self administration | minor | major | new, enable, support |
| WI00809931 | Easy - validation and wording changes for CDS | minor | major | new, add |
| WI00862249 | S&S GB - change in mapping to better support multiple commodities | minor | major | new, add, support |
| WI00795931 | Improve Label Printing Speeds for Forwarding | minor | major | new, add, support |
| WI00887209 | Turn off Audit Events for Declaration tables | minor | major | add, enable, support |
| WI00883044 | Removing Audit Event (ADD/EDT/DEL) Logs from AccChargeCode Table | minor | major | add |
| WI00904060 | Total Allocation Statistics Section UI Enhancements | minor | major | support |
| WI00885380 | AM:(SL) Remove Manual Logging of ADD/EDT/DEL Logs | minor | major | new, add |
| WI00882702 | Add 'Audit Data' tab in AR/AP Journal form | minor | major | add |
| WI00882716 | Add 'Audit Data' tab in CB Direct Receipt/ Payment form | minor | major | add |
| WI00832175 | FR - TP5 - Message IE034 | minor | major | P5, TP5 |
| WI00961975 | AccQueryClaim-Audit Data tab & AAL AEL event & Data Transformation | minor | major | new, add |
| WI00880423 | JP Common - Send with Message Error Security Item | minor | major | enable |
| WI00961979 | AccHotCheque-Audit Data tab & AAL AEL event & Data Transformation | minor | major | new, add |
| WI00840684 | CT Status to be included in FHL messages for exports from IT | minor | major | \bcompliance\b, new, add |
| WI00953180 | AE Manifest - Add Messages sub tab to the Main>Bills tab | minor | major | add |
| WI00840027 | [EAD] Add Transport Type to EDI Message | minor | major | new, add, schema |
| WI00913271 | DMN: Update the log message in DED Service Task | minor | major | new |
| WI00887294 | Turn off Audit Events for Global Manifest tables | minor | major | add, enable |
| WI00887294 | Turn off Audit Events for Global Manifest tables | minor | major | add, enable |
| WI00841200 | [S2S] Customer Integrated Applications Documentation | minor | uncertain |  |
| WI00884121 | TW - Minor fix captions | minor | major | add |
| WI00894087 | Update note: CargoWise upgrade package 25.4.7 released | minor | uncertain |  |
| WI00854985 | PP: Expose Distribution Center field to be added on Warehouse Order reports | minor | major | add |
| WI00931123 | Add 'Audit Data' tab in CB Deposit Batch form | minor | major | new, add |
| WI00886436 | Enable Audit Data tab for all JobDeclaration Forms | minor | major | add, enable, support |
| WI00963511 | DMN:(DTG) OM Add Date Required to doc tracking filters in search grid | minor | major | add |
| WI00906469 | Add CusLiquidation and CusPackingList to Declaration Audit Tab | minor | major | add, enable |
| WI00905209 | PP: Expose the Pick Priority Macros on order documents | minor | major | add |
| WI00858958 | Minor Registry Defaults Change EMCS S&S GB and CDS Cash & PVA Payments Ledger | minor | major | new, enable, support |
| WI00842855 | EDI Message Purge Settings - IL Core | minor | major | new, add, R3 |
| WI00883042 | Removing Audit Event (ADD/EDT/DEL) Logs from AccBankAccount Table | minor | major | add |
| WI00842522 | MDM Compliance? Message Purge Settings For DPS and CPW | minor | major | \bcompliance\b, add, compliance |
| WI00820953 | eTail V2 HCH_ScanCompleteTime column is exposed for updates via trigger | minor | major | new, add, support |
| WI00795931 | Improve Label Printing Speeds for Forwarding | minor | major | new, add, support |
| WI00883055 | Removing Audit Event (ADD/EDT/DEL) Logs from AccTaxOverrideGroup Table | minor | major | add, tax |
| WI00869781 | GSS API: Expose CfsCutOff, HazCutOff, and ReeferCutOff in GSS API | minor | major | new, add, convert |
| WI00907575 | TM2: Expose Receive Dock Door | minor | major | add, enable, support |
| WI00928137 | Adding UsingIndexFilters column and filter to Tag Rules Module | minor | major | add |
| WI00901513 | Registries, messages and hint adjustments for reopen period self administration | minor | major | new, enable, support |
| WI00866116 | SeaShanty: amend mapping for EVGL event "despatch by..." and "Full import contai | minor | major | add |
| WI00899932 | Inhibit silly users sending second original (NEW) message to CDS | minor | major | new, add |
| WI00883046 | Add 'Audit Log' tab in Compliance Document Header form | minor | major | \bcompliance\b, new, add |
| WI00932481 | Add 'Audit Data' tab in Job Revenue Journal form | minor | major | new, add |
| WI00795736 | Stop logging audit on OrgContact | minor | major | new, add, enable |
| WI00856054 | Audit: Audit Data tab shows more than one month of data | minor | major | support |
| WI00825100 | TW [CUS][DEF] Import Date validation | minor | major | support |
| WI00959449 | TW [CUS][DEF] Net Weight Defaulting | minor | major | support |
| WI00879534 | Stop logging Audit event for OrgDebtorGroup, OrgCreditorGroup and OrgCollectionN | minor | uncertain |  |
| WI00908731 | [AU] Add new Referral reason column to form and send in message | minor | major | new, add |
| WI00809931 | Easy - validation and wording changes for CDS | minor | major | new, add |
| WI00910026 | Turn off Audit Events for Exit Control | minor | major | add, enable |
| WI00883049 | Removing Audit Event (ADD/EDT/DEL) Logs from AccGLBudget Table | minor | major | add |
| WI00832175 | FR - TP5 - Message IE034 | minor | major | P5, TP5 |
| WI00962205 | Adjust DLY event update note | minor | major | new, add, support |
| WI00905356 | Removal of BIN prefix from FWB and FHL for air shipments to Bangladesh | minor | major | \bcompliance\b, new, compliance |
| WI00883045 | Removing Audit Event (ADD/EDT/DEL) Logs from AccChequeBook Table | minor | major | add |
| WI00920447 | [DOS] Document Signing Service - Change Digital Signature Wording | minor | major | new, add, support |
| WI00943711 | Identify preferred UNLOCO per Carrier EDI Code Mapping for GSS Import | minor | major | new, add, convert |
| WI00832513 | [HK] Update message sender to use ACAS data Part 1 | minor | major | new, add, support |
| WI00862005 | Debtor defaulting behaviour in charge line for inter company AP posting | minor | major | add |
| WI00795908 | [INC] Set Awaiting Response without sending a message fix | minor | major | enable, support |
| WI00842164 | IT (NCTD5 TP OFF) add House>CountryOfDestination in GUI and message C0343 | minor | major | add |
| WI00908999 | IT (WHS) Validations on Warehouse tab in Organization | minor | major | R2 |
| WI00891640 | AU COLS UCMP - Enable Packing EDIMessage to EDIInterchange via UCMP | minor | major | enable |
| WI00973374 | Brazil - XUT - Add Compliance Book Node to include compliance Book Prefix | minor | major | \bcompliance\b, add, compliance |
| WI00859945 | [TKN] WiseCloud Token Client supports multiple domain hints | minor | major | new, add, support |
| WI00883050 | Add 'Audit Log' tab in General Ledger Account form | minor | major | new, add |
| WI00870699 | TW [CUS][ENH] - Enhance error messages - Suggestions | minor | major | add, support, tax |
| WI00912098 | GCT: validation for ATD - actual DEP cannot be before GOU CY/GIN CTO (origin) | minor | major | new, add, enable |
| WI00821302 | Vessel Stow Plan - allow deletion of BLs before sending message | minor | major | support |
| WI00961973 | AccCollectionBatch-Audit Data tab & AAL AEL event & Data Transformation | minor | major | new, add |
| WI00882704 | Add 'Audit Data' tab in AR/AP Transfer form | minor | major | add |
| WI00939796 | Deprecated columns in Audit are removed as part of the audit retention process | minor | major | new, add |
| WI00882709 | Add 'Audit Data' tab in AR/AP OVP/EXX/DSC form | minor | major | add |
| WI00975359 | add MID add, query options to UXML data Import | minor | major | add, support |
| WI00882708 | Add 'Audit Data' tab in AR/AP INV/CRD/ADJ form | minor | major | add, enable |
| WI00863826 | Add Client Side Date Validation To Android | minor | major | new, add, support |
| WI00939929 | TW [CUS][DEF] NX5901 Upload File validation | minor | major | add |
| WI00973468 | DE IMPORT - Add Validation for Deferral Account Payment Party2 | minor | major | add, P5 |
| WI00963944 | Remove update note CargoWiseOneUpdateNote20200616c | minor | major | new |
| WI00878517 | TR e-INV - Adding Validation For AP CRD with DAR/DIN Sub Type | minor | major | add, enable, e-?invoice |
| WI00882719 | Add 'Audit Data' tab in CB Direct Debit Batch form | minor | major | add |
| WI00883052 | Removing Audit Event (ADD/EDT/DEL) Logs from AccInvMsg Table | minor | major | add |
| WI00883047 | Removing Audit Event (ADD/EDT/DEL) Logs from AccComplianceSequence Table | minor | major | add, compliance |
| WI00939877 | Turn off Audit Events for CusTempStorage | minor | major | add, enable, R2 |
| WI00943148 | [MYA.SSO] New audit data subscriber service task for user account report | minor | major | new, add, support |
| WI00882707 | Add 'Audit Data' tab in AR/AP Receipt/Payment form | minor | major | add |
| WI00882705 | Add 'Audit Data' tab in AR/AP Contra form | minor | major | add |
| WI00825620 | CN - Find function for Message | minor | major | add, enable, support |
| WI00870671 | Universal Transaction Batch (XUB) - Defaulting Branch and Department | minor | major | support |
| WI00888284 | Add FAQ to .NET 8 update note | minor | major | add, support |
| WI00918300 | GCT: ArrivalAfterUnloadEventValidator convert to AUX | minor | major | new, add, support |
| WI00930592 | Costa Rica - Update Defaulting Rules RECEIVABLES | minor | major | \bcompliance\b, compliance |
| WI00934757 | CT Status to be included in OCI segment of direct FWB messages for IT exports | minor | major | \bcompliance\b, new, add |
| WI00887294 | Turn off Audit Events for Global Manifest tables | minor | major | add, enable |
| WI00884121 | TW - Minor fix captions | minor | major | add |
| WI00836912 | CPR - Update Documentation to link to WTA | minor | major | add |
| WI00869797 | FR e-Inv - Suffixe and Routage | minor | major | new, add |
| WI00883053 | Add 'Audit Log' tab in AR/AP Payment form | minor | major | new, add, support |
| WI00938184 | CC:Improve Result Message & Display Error Logs/Reasons in the Cycle Count Module | minor | major | new, add |
| WI00894087 | Update note: CargoWise upgrade package 25.4.7 released | minor | uncertain |  |
| WI00882713 | Add 'Audit Data' tab in CB Opening Receipt/ Payment form | minor | major | add |
| WI00871680 | IE UCC5: Add data elements to captions Part 3 | minor | major | add |
| WI00883054 | Removing Audit Event (ADD/EDT/DEL) Logs from AccPeriodManagement Table | minor | major | add |
| WI00921987 | Update Note for new Unload Completed Prompt on RF | minor | major | \bnew\ feature\b, new, add |
| WI00899991 | CN - Add a filter "Report Setup" to GL Multi-Language Mapping Module | minor | major | add |
| WI00861419 | Add Staff Assignments - Product filters | minor | major | new, add |
| WI00938043 | Extend Audit Tab for other entities besides the Parent Object | minor | major | add, enable |
| WI00854985 | PP: Expose Distribution Center field to be added on Warehouse Order reports | minor | major | add |
| WI00857418 | [Lead Job] Validation Tool Phase 2 | minor | major | Phase 2 |
| WI00852464 | Update Note for Enable Row Name Prefix Validation for Fixed Width Warehouses | minor | major | new, enable |
| WI00846300 | [EAD][INC] Universal Shipment Request Response to support EDI Message Profile | minor | major | add, support, schema |
| WI00846197 | CW to CW: Update matching logic for subsquent messages (AMD, BR SI) | minor | major | add |
| WI00879484 | FB: add validation for Container volume in BR and SI forms | minor | major | add, bulk |
| WI00879484 | FB: add validation for Container volume in BR and SI forms | minor | major | add, bulk |
| WI00811632 | Update Update Note | minor | uncertain |  |
| WI00812715 | Mobility: Fix for Multiple App Issues | minor | major | \bnew\ feature\b, new, add |
| WI00909439 | Document Delivery to eDocs: type PDF no longer defaults | minor | major | new, enable, support |
| WI00838626 | [AuditLogs] Turn Off Audit logs for workflow tables | minor | major | new, add, enable |
| WI00915965 | Update Note Index search for Tag Rules module | minor | uncertain |  |
| WI00830736 | TB - Container Transport Optimization Validation - Container Number | minor | major | add |
| WI00916897 | Deliver second actual CAV (either from terminal or carrier) as AUX event. | minor | major | new, add, enable |
| WI00810124 | L&A PM: Port Authority message - IFCSUM Additional Fields Kembla port AUPKL | minor | major | add |
| WI00916897 | Deliver second actual CAV (either from terminal or carrier) as AUX event. | minor | major | new, add, enable |
| WI00876961 | FB: Reefer Settings (Air Vent & Humidty) display and validations | minor | major | \bnew\ form\b, new, add |
| WI00931645 | eTail V2 Fix Org Matching update note | minor | major | new, add, enable |
| WI00828872 | AM:(SL) Add List of Missing Tables to Audit Database | minor | major | add |
| WI00828872 | AM:(SL) Add List of Missing Tables to Audit Database | minor | major | add |
| WI00828872 | AM:(SL) Add List of Missing Tables to Audit Database | minor | major | add |
| WI00828872 | AM:(SL) Add List of Missing Tables to Audit Database | minor | major | add |
| WI00828872 | AM:(SL) Add List of Missing Tables to Audit Database | minor | major | add |
| WI00828872 | AM:(SL) Add List of Missing Tables to Audit Database | minor | major | add |
| WI00942295 | [EAD][UI] Rename Registry root element & Service Task Product Area | minor | major | add |
| WI00893542 | [HS-Prio] CWNext - Release Notes | minor | uncertain |  |
| WI00893542 | [HS-Prio] CWNext - Release Notes | minor | uncertain |  |
| WI00893542 | [HS-Prio] CWNext - Release Notes | minor | uncertain |  |
| WI00836450 | [UXML] Add and Apply "Remove Empty XML Elements" Settings on EDI Message Profile | minor | major | add |
| WI00823977 | [AuditLogs] Deprecate Audit Log - TAN and UPN | minor | major | add, support |
| WI00973285 | [ERQ.2] Release 1 Documentation | minor | uncertain |  |
| WI00973285 | [ERQ.2] Release 1 Documentation | minor | uncertain |  |
| WI00795589 | [AuditLogs] Turn off Audit Logs for Work Items | minor | major | R3 |
| WI00874989 | AVS: Remove logging to Microsoft Teams | minor | major | add |
| WI00887282 | [End-to-End Testing + Update Note] Ability to override assigned Dock Door locati | minor | uncertain |  |
| WI00837367 | [EAD] Accept Individual EDI Message Types in eAdaptorNext Async | minor | major | add, support |
| WI00831540 | Airline Connect -No flight update nor message logs | minor | major | add |
| WI00837349 | The GLOW > Services > Indexing Service now defaults to Yes | minor | major | add, enable, support |
| WI00895587 | L&A PM: Port Authority Message - IFCSUM Discharge for Port Kembla | minor | major | new, add |
| WI00898548 | Audit Tab log does not capture multiple tabs changes | minor | major | new, add, support |
| WI00934227 | FB: ease validation on HBL field in CargoNaut form | minor | major | add |
| WI00930630 | update note | minor | uncertain |  |
| WI00923471 | [EAD][EDI Client] Remove Mentioning of CR9 in EDI Client Guide | minor | uncertain |  |
| WI00923471 | [EAD][EDI Client] Remove Mentioning of CR9 in EDI Client Guide | minor | uncertain |  |
| WI00800513 | Verbose logging for carrier | minor | major | add, enable |
| WI00802540 | GLWOM: SPT Import Existing Consol - Additional Filters | minor | major | new, add, support |
| WI00943485 | DD Certification: CPTPP Update note | minor | uncertain |  |
| WI00819901 | TB: Change TPT Mode caption to 'Transport Mode' | minor | major | add |
| WI00852566 | Report Management Module supports Index Search Filters | minor | major | support |
| WI00852566 | Report Management Module supports Index Search Filters | minor | major | support |
| WI00887085 | Enable Audit Data tab for all Global Manifest (and related) Forms | minor | major | add, enable, tax |
| WI00889161 | EU AIS/AES - Supporting/Previous documents defaulting | minor | major | support |
| WI00872105 | Delta: CMR Consignment Note - Mapping - Transport Booking | minor | major | add |
| WI00853193 | Rename CargoWiseOne.ServiceManager.Host.exe | minor | major | add |
| WI00903278 | GLWOM: Request Phase 2  Part 3 UI Change for Request Type and Validation Rules | minor | major | new, add, support |
| WI00903278 | GLWOM: Request Phase 2  Part 3 UI Change for Request Type and Validation Rules | minor | major | new, add, support |
| WI00832088 | FB: Introduce validations on HBL form | minor | major | add |
| WI00894067 | [EAD][ADH] EDI Message Profile Data Context improvements | minor | major | add, support, schema |
| WI00852543 | [DateTimes] UXML Task, Milestone and Exception support offsets | minor | major | support |
| WI00852543 | [DateTimes] UXML Task, Milestone and Exception support offsets | minor | major | support |
| WI00857556 | Publish Update Note - XCG Currency Code Introduced | minor | major | new, add, support |
| WI00908473 | [WIN] Documentation for Onboarding module for other teams for B2C | minor | major | enable |
| WI00908473 | [WIN] Documentation for Onboarding module for other teams for B2C | minor | major | enable |
| WI00877025 | Remove Audit Event (ADD/EDT/DEL) Logs from StmALog Table - IL Core | minor | major | add, enable |
| WI00881780 | ACAS - Item 9 - Customer Account Shipping Frequency [Slow PrintFinalMaster FIX] | minor | major | new, add |
| WI00862575 | Scale out - use of secondary 'more broadly' - Module Search Filters | minor | major | add, enable, support |
| WI00802640 | [AuditLogs] Add Audit Data Tab For Templates | minor | major | new, add, support |
| WI00802351 | Remove eServices > Universal XML > Enable DateTime Offset in Outbound Messages | minor | major | add, enable |
| WI00865981 | GLWOM: CLP add location filters for booking information | minor | major | new, add |
| WI00822867 | [EAD] Add UTC Unix Timestamp in all UXML/NXML | minor | major | new, add, enable |
| WI00887276 | Turn off Audit Events for Product tables | minor | major | new, add, enable |
| WI00966808 | Update EDI Client guide to include CSR format requirement | minor | major | add, support |
| WI00944501 | [HS] CWNext RecentMessages: improve performance of refresh | minor | major | add, support |
| WI00943484 | DD Certification: COONZ Update note | minor | uncertain |  |
| WI00852607 | IOM [UPS] - Container Load List & Container Load Plan Filters | minor | major | add, support |
| WI00909031 | [FTS]Display max records returned message in module query | minor | major | add, enable |
| WI00946122 | DD.CERT.CW: Create update note for PAFTA Cert type | minor | major | add, R2 |
| WI00819182 | VTP: UXml missing addrss fields - CW1 update | minor | major | add, support |
| WI00849721 | Logging Enhancement | minor | major | add |
| WI00946262 | WCA Update Note /extract option is out of date | minor | uncertain |  |
| WI00930399 | FB: Ease validations for Port of Lyttelton Export Pre-Advice | minor | major | new, add |
| WI00946539 | POH: End to End Testing and Update Note | minor | uncertain |  |
| WI00950408 | AM:(STM) Publish Update Note | minor | major | enable |
| WI00903310 | Update SpeeDee connector to new CMB requirements | minor | major | new |

## Examples (first 20 rows)

| WorkItem | Summary | Predicted | Matched patterns | Explanation snippet |
|---|---|---:|---|---|
| WI00818184 | CPW: ComplianceWise enabled by default and support only | major | \bComplianceWise\b, new, enable | New or updated regulatory framework |
| WI00818184 | CPW: ComplianceWise enabled by default and support only | major | \bComplianceWise\b, new, enable | New or updated regulatory framework |
| WI00862744 | EG e-Invoice - Add Bank Account Details to AR e-Invoice Submission XML | major | new, add, support | New or updated regulatory framework |
| WI00904060 | Total Allocation Statistics Section UI Enhancements | major | support | Minor tweak to existing behaviour |
| WI00817855 | Colombia - New IVA Withholding RETEIVA General Rate | major | \bcompliance\b, new, add | Country COLOMBIA  Sub Project HYPERLINK "edient:Command=ShowEditForm&LicenceCode=EDIAG0SYD&Controlle |
| WI00947734 | EU ICS2 - R3 - F40/F41 Conformance test and UPN | major | \bICS2\b, new, regulatory | New or updated regulatory framework |
| WI00887209 | Turn off Audit Events for Declaration tables | major | add, enable, support | Logging or audit-only change |
| WI00829485 | [CCA] Consol ETD should NOT check Allocation Route Period if Booking/MBL exist | minor | fix, validation | Done Statement  Once the Carrier Booking Number or Master Bill of Lading Number existed on the Conso |
| WI00871784 | IT (NCTD5 TP OFF) Registration date for amendment without declaration | uncertain |  | DONE STATEMENT  When user must amend a declaration done in another system he sets a declaration with |
| WI00892617 | MEXICO - New TAX ID to calculate 8% VAT (IVA) AND "2/3" IVA withholding (5.33%) | major | \bcompliance\b, new, support | Tax/VAT or compliance regime change |
| WI00936329 | not able to send Country of Destination if different from Consignee | uncertain |  | see eDocs. |
| WI00872057 | PP: Stock on Hand Report By Location and Stock Movement Report | major | new, add | AQO 30-Apr-25 09:29 GMT+10:00:   for functional review  1. the "Stock Movement Report" has been upda |
| WI00872057 | PP: Stock on Hand Report By Location and Stock Movement Report | major | new, add | AQO 30-Apr-25 09:29 GMT+10:00:   for functional review  1. the "Stock Movement Report" has been upda |
| WI00889253 | CCSUK (temporary storage) pre- vs post-arrivals | major | new, add | CKG 03-Apr-25 10:36 GMT+01:00:     Tech Design:    1, The field we need to add the validation to is  |
| WI00934170 | AM: (STM) Collect null values in S7_OpenDateTimeUtc | major | new, add | KGG 09-Jul-25 09:13 GMT+10:00:   In HYPERLINK "edient:Command=ShowEditForm&ControllerID=NewWorkItem& |
| WI00928789 | Dangerous Goods: RID 2025 Reference data update | major | \bDangerous\ Goods\b, \bcompliance\b, new | New or updated regulatory framework |
| WI00853749 | MAWB Form - Shipper and Consignee Account No. fields (ACAS item 7 support) | major | add, support | AFE 14-Jan-25 16:16 GMT+08:00:    # Done statements    As per HYPERLINK "edient:Command=ShowStorageD |
| WI00853749 | MAWB Form - Shipper and Consignee Account No. fields (ACAS item 7 support) | major | add, support | AFE 14-Jan-25 16:16 GMT+08:00:    # Done statements    As per HYPERLINK "edient:Command=ShowStorageD |
| WI00865431 | GCT Turn AUX WhiteList into BlackList | major | new, add, support | Minor tweak to existing behaviour |
| WI00818184 | CPW: ComplianceWise enabled by default and support only | major | \bComplianceWise\b, new, enable | New or updated regulatory framework |
