    public AFD toAFD() throws Exception {
        this.rename();
        ArrayList<Liaison> AFDvers=new ArrayList<Liaison>(0);//la liste de liaison version AFD
        ArrayList<Character> mots=this.getMots();//la liste des mots du langage
        ArrayList<Etat> etats=new ArrayList<Etat>(0);//la liste des états de l'AFD
        etats.add(new Etat(etatInit.getNom(),etatInit.isTerminal()));
        for (int i=0;i<etats.size();i++) {//pour chaque état si je peux créer un nouvel état je l'ajoute et j'essaie de créer encore un nouvel état
            for (char m:mots) {//pour chaque mot du langage
                boolean ajout=false;//par défaut je n'ai pas ajouté d'état
                Etat toAdd=new Etat("",false);//je prépare l'état à ajouter sinon le compilateur ne sais pas s'il est initialisé
                for (Liaison l:liaisons) {
                    if(!ajout&&l.getMot()==m){//si je n'ai pas encore ajouté et que le mot de la liaison est bonne
                        for (String nom:etats.get(i).getNom().split(",")) {//je vérifie si le nom de l'état intermédiaire contient le nom de l'état de la liaison
                            if (l.getAvant().getNom().equals(nom)){
                                toAdd=new Etat(l.getApres().getNom(),l.getApres().isTerminal());//si oui je prépare l'ajout de l'état
                                ajout=true;
                            }
                        }
                    } else if (ajout&&l.getMot()==m) {//et s'il y a d'autre liaison par cet état avec cette même liaison
                        for (String nom:etats.get(i).getNom().split(",")) {
                            if (l.getAvant().getNom().equals(nom)){
                                toAdd.setNom(toAdd.getNom()+","+l.getApres().getNom());//je crée un état intermédiaire qui va s'appeler premierétat,deuxièmeétat
                                if(l.getApres().isTerminal()){
                                    toAdd.setTerminal(true);
                                }
                            }
                        }
                    }
                }
                if(ajout){//si on a créé un nouvel état à ajouter
                    boolean estDedans=false;//je vérifie si l'état existe déjà parmis les états que j'ai créé
                    for (Etat E:etats) {
                        boolean egal=true;
                        for (String eNom:E.getNom().split(",")) {
                            boolean motDedans=false;
                            for (String addNom:toAdd.getNom().split(",")) {
                                if(eNom.equals(addNom)){
                                    motDedans=true;
                                    break;
                                }
                            }
                            if (!motDedans){
                                egal=false;
                                break;
                            }
                        }if(egal){
                            for (String addNom:toAdd.getNom().split(",")) {
                                boolean motDedans=false;
                                for (String eNom:E.getNom().split(",")) {
                                    if(eNom.equals(addNom)){
                                        motDedans=true;
                                        break;
                                    }
                                }
                                if (!motDedans){
                                    egal=false;
                                    break;
                                }
                            }
                        }
                        if (egal){//si l'état existe déjà, l'état à ajouter devient l'état existant déjà
                            toAdd=E;
                            estDedans=true;
                            break;
                        }
                    }
                    if(!estDedans)
                        etats.add(toAdd);
                    AFDvers.add(new Liaison(etats.get(i),toAdd,m));//dans tous les cas je crée la nouvelle liaison
                }
            }
        }
        AFD a=new AFD(AFDvers,etats.get(0));
        a.rename();
        return a;
    }