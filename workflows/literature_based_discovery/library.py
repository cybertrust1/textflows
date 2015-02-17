from workflows.literature_based_discovery.lib.heuristics.heuristic_calculations import HeuristicCalculations
from workflows.textflows import flatten


def lbd_heuristics_selection(input_dict):
    return {}

def lbd_heuristic_selection_post(postdata, input_dict, output_dict):
    widget_id = postdata.get('widget_id')[0]
    selected_heuristics=postdata.get('selected[]',[])

    return {'heuristics': selected_heuristics}


def lbd_heuristic_min(input_dict):
    heuristic_names=flatten(input_dict.get('heuristics',[]))
    return {'heuristic': ('Min',heuristic_names)}

def lbd_heuristic_max(input_dict):
    heuristic_names=flatten(input_dict.get('heuristics',[]))
    return {'heuristic': ('Max',heuristic_names)}

def lbd_heuristic_sum(input_dict):
    heuristic_names=flatten(input_dict.get('heuristics',[]))
    return {'heuristic': ('Sum',heuristic_names)}

def lbd_heuristic_norm(input_dict):
    heuristic_names=flatten(input_dict.get('heuristics',[]))
    return {'norm_heuristics': [('Norm',heuristic_name) for heuristic_name in heuristic_names]}

def lbd_ensemble_heuristic_vote(input_dict):
    heuristic_names=flatten(input_dict['heuristics'])
    return {'heuristic': ('Vote',heuristic_names)}

def lbd_ensemble_average_position(input_dict):
    heuristic_names=flatten(input_dict['heuristics'])
    return {'heuristic': ('AvgPos',heuristic_names)}

def lbd_calculate_heuristics(input_dict):
    heuristic_names=input_dict.get('heuristics',[])
    adc=input_dict['adc']
    bow_model=input_dict['bow_model']

    raw_documents=bow_model.get_raw_text(adc.documents)
    classes=bow_model.get_labels(adc,binary=True)

    hc=HeuristicCalculations(raw_documents,classes,bow_model)
    calcs=hc.calculate_heuristics(heuristic_names)
    return {'calcs': calcs}

def lbd_actual_and_predicted_values(input_dict):
    bterms=input_dict['bterms']
    bow_model=input_dict['bow_model']
    vocabulary=bow_model._vocab_to_idx()

    actual_values=[0]*len(vocabulary)
    for bterm in bterms:
        if bterm in vocabulary:
            actual_values[vocabulary[bterm]]=1
            print bterm

    heuristics=flatten(input_dict['heuristics'])

    return {'apv':[{'name': h.name,'predicted':list(h.scores),'actual':actual_values} for h in heuristics]}

def lbd_explore_in_crossbee(input_dict):
    from workflows.textflows_dot_net.serialization_utils import ToNetObj
    import LatinoInterfaces
    output_dict={}
    output_dict['serialized_adc']=LatinoInterfaces.LatinoCF.Save(ToNetObj(input_dict['adc']))#.serialized_object
    output_dict['vocabulary']=[kv[1] for kv in sorted(input_dict['bow_model']._idx_to_vocab().items())]
    output_dict['heuristic_scores']=[{'name': hevr.name, 'scores': hevr.scores.tolist()} for hevr in flatten(input_dict['heuristic_scores'])]
    output_dict['bterms']=input_dict['bterms']
    return output_dict
    #return render(request, 'visualizations/open_data_in_crossbee.html',{'widget':widget}) #,'input_dict':input_dict,'output_dict':output_dict})