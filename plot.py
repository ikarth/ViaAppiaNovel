import settings
import collections
import math
import itertools


plotting = {}
plotting['introduce need'] = {'substeps':None, 'halt': 'EVENT-EXPLAIN GOAL'}
plotting['have need'] = {'substeps':[['introduce need','new macguffin', 'fulfill need']], 'halt': False}
#plotting['hunt macguffin'] = {'substeps':[['new macguffin'], ['new macguffin', 'new macguffin', 'combine macguffins']], 'halt': 'EVENT-MACGUFFIN HUNT FAIL'}
#plotting['get parts for macguffin'] = {'substeps':[['macguffin hunt scene'], ['hunt macguffin', 'hunt macguffin'], ['macguffin hunt scene']], 'halt': 'EVENT-MACGUFFIN HUNT SCENE-SUCCESS' }
plotting['fulfill need'] = {'substeps':None, 'halt': 'EVENT-FULFILL GOAL'}
plotting['new macguffin'] = {'substeps':[['introduce macguffin', 'macguffin hunt']], 'halt': 'EVENT-MACGUFFIN HUNT FAIL'}
plotting['introduce macguffin'] = {'substeps':None, 'halt': 'EVENT-INTRODUCE MACGUFFIN'}
plotting['combine macguffin'] = {'substeps':None, 'halt': 'EVENT-COMBINE MACGUFFIN'}
#plotting['assemble macguffin'] = {'substeps':[['hunt macguffin', 'hunt macguffin'], ['macguffin hunt scene', 'assemble macguffin']], 'halt': 'EVENT-MACGUFFIN ACQUIRED'}
plotting['macguffin hunt'] = {'substeps':[['new macguffin', 'new macguffin', 'combine macguffin'], ['macguffin hunt failure', 'macguffin success']], 'halt': 'EVENT-MACGUFFIN ACQUIRED'}
plotting['macguffin success'] = {'substeps':None, 'halt': 'EVENT-MACGUFFIN ACQUIRED'}
plotting['macguffin hunt failure'] = {'substeps':[['macguffin hunt failure'],['macguffin hunt failure'],['macguffin hunt failure', 'macguffin hunt failure']], 'halt': 'EVENT-MACGUFFIN HUNT FAIL'}

events = {"EVENT-EXPLAIN GOAL":{'sort':0, 'progress':0},
          'EVENT-DEUS EX MACHINA MACGUFFIN':{'sort':2, 'progress':0},
          'EVENT-MACGUFFIN ACQUIRED':{'sort':3, 'progress':1},
          'EVENT-FULFILL GOAL':{'sort':9, 'progress':1},
          'EVENT-INTRODUCE MACGUFFIN':{'sort':1, 'progress':0},
          'EVENT-COMBINE MACGUFFIN':{'sort':3, 'progress':1},
          'EVENT-MACGUFFIN HUNT FAIL':{'sort':2, 'progress':1}}


macguffin_count = 0
def expandStep(step):
    """
    Return either the plot step or its expansion.
    """
    global macguffin_count
    #print(step['goal'])
    #print(step['layer'])
    if plotting[step['goal']]:
        if plotting[step['goal']]['substeps']:
            pick = settings.TRAVEL_RNG.choice(range(len(plotting[step['goal']]['substeps'])))
            result = plotting[step['goal']]['substeps'][pick]
            #print(result)
            m_count = step['layer']
            m_target = int(step['target'])
            if str(result[0]) == 'introduce macguffin':
                macguffin_count += 1
                m_count = macguffin_count
                m_target = int(step['layer'])
            return [{'goal':i, 'layer':m_count, 'target':m_target} for i in result]
    return [step]

def haltPlotExpansion(plot):
    """
    Convert a plot into a series of events
    """
    event_list = []
    fail_expand = 0
    for step in plot:
        if plotting[step['goal']]:
            if plotting[step['goal']]['halt'] != False:
                event_list.append({'goal':plotting[step['goal']]['halt'], 'layer':step['layer'], 'target':step['target'], 'sort':0})
                continue
        event_list.append(step)
        fail_expand += 1
    return event_list, (fail_expand < 1)

def reorderPlot(plot):
    """
    Take the finished plot-event tree and reorder some of the steps.
    It can do this because the steps know which layer they are on,
    and their target layer (which is also their parent layer).
    """
    max_layer = macguffin_count
    if 1 + (max_layer * max_layer * 99) < 0:
        print ("Warning: End integer wrap likely")
    #sort_weights = [((i['target']*max_layer*100) + i['layer']) for i in plot]
    counter = 0

    sort_layers = {0:0}
    for i in plot:
        if i['goal'] == 'EVENT-INTRODUCE MACGUFFIN':
            if i['target'] in sort_layers:
                sort_layers[i['layer']] = sort_layers[i['target']] + 1
            else:
                sort_layers[i['layer']] = 0
    #print (sort_layers)

    for idx, i in enumerate(plot):
        i['sort'] = sort_layers[i['layer']]
        i['progress'] = events[i['goal']]['progress']

        #counter += 1
        #i['sort'] = counter
        #if i['goal'] == 'EVENT-FULFILL GOAL':
        #    i['sort'] = (max_layer * max_layer * 99) + 1
        #else:
        #    i['sort'] = sort_layers[i['layer']]
             
    #print(plot)
    #sorted(plot, key=lambda k: k['sort'])
    sorted_plot = plot

    return sorted_plot


def expandPlot(current_plot):
    """
    Given a plot array, expand it one step.
    """
    new_plot = []
    for i in current_plot:
        new_plot.extend(expandStep(i))
    return new_plot



def createPlot(length):
    global macguffin_count
    macguffin_count = 0
    a_current_plot = [{'goal':'have need','layer':macguffin_count,'target':-1}]
    final_plot = []
    plot_is_too_short = True
    counter = 0
    while plot_is_too_short:
        counter += 1
        final_plot, success = haltPlotExpansion(a_current_plot)
        a_current_plot = expandPlot(a_current_plot)
        if len(a_current_plot) > length and success == True:
            plot_is_too_short = False
        if counter > 25:
            print("Warning: Plot loop exceeded safeguards")
            break
    final_plot = reorderPlot(final_plot)
    return final_plot

def testPlot():
    global macguffin_count
    macguffin_count = 0
    a_current_plot = [{'goal':'have need','layer':macguffin_count,'target':-1}]
    for i in range(0,7):
        a_current_plot = expandPlot(a_current_plot)
        print("[=>" + str(a_current_plot) + "<")

    for i in a_current_plot:
        print(str("   " * i['target']) + str(i['goal']) + " #" + str(i['layer']) + "\t\tparent: " + str(i['target']))

    final_plot, success = haltPlotExpansion(a_current_plot)
    print("-----------")

    for i in final_plot:
        print(str("   " * i['target']) + str(i['goal'])[6:] + " #" + str(i['layer']) + "\t\tparent: " + str(i['target']) + "\tsort: " + str(i['sort']))
    print("-----------")
    #final_plot = reorderPlot(final_plot)
    #for i in final_plot:
    #    print(str("   " * i['target']) + str(i['goal'])[6:] + " #" + str(i['layer']) + "\t\tparent: " + str(i['target']) + "\tsort: " + str(i['sort']))
    