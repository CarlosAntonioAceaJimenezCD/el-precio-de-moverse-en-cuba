package com.ermetic.circuitoshabana.data;

import androidx.compose.ui.tooling.preview.AndroidUiModes;
import com.ermetic.circuitoshabana.service.AlarmaCircuito;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import kotlin.Metadata;
import kotlin.Pair;
import kotlin.collections.CollectionsKt;
import kotlin.collections.SetsKt;
import kotlin.jvm.functions.Function1;
import kotlin.jvm.internal.Intrinsics;
import kotlin.text.StringsKt;

/* JADX INFO: compiled from: Traspasos.kt */
/* JADX INFO: loaded from: classes2.dex */
@Metadata(d1 = {"\u0000L\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0007\n\u0002\u0010\"\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010 \n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\t\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0005\bÇ\u0002\u0018\u00002\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u0003J\u000e\u0010\u000f\u001a\u00020\u00102\u0006\u0010\u0011\u001a\u00020\u000eJ\u0014\u0010\u0012\u001a\b\u0012\u0004\u0012\u00020\u000e0\u00132\u0006\u0010\u0014\u001a\u00020\u000eJ\u0016\u0010\u0015\u001a\b\u0012\u0004\u0012\u00020\u000e0\u00132\u0006\u0010\u0011\u001a\u00020\u000eH\u0002J\u0010\u0010\u0016\u001a\u00020\u00102\u0006\u0010\u0017\u001a\u00020\u000eH\u0002J\u000e\u0010\u0018\u001a\u00020\u000e2\u0006\u0010\u0011\u001a\u00020\u000eJ\u0016\u0010\u0019\u001a\u00020\u001a2\u0006\u0010\u0011\u001a\u00020\u000e2\u0006\u0010\u001b\u001a\u00020\u001cJJ\u0010\u001e\u001a\b\u0012\u0004\u0012\u00020\u001f0\u00132\f\u0010 \u001a\b\u0012\u0004\u0012\u00020\u001f0\u00132\f\u0010!\u001a\b\u0012\u0004\u0012\u00020\u001f0\u00132\u0018\u0010\"\u001a\u0014\u0012\u0010\u0012\u000e\u0012\u0004\u0012\u00020\u000e\u0012\u0004\u0012\u00020\u001c0#0\u00132\u0006\u0010$\u001a\u00020\u001cJ\u0016\u0010%\u001a\u00020\u000e2\u0006\u0010&\u001a\u00020\u001f2\u0006\u0010'\u001a\u00020\u000eR\u000e\u0010\u0004\u001a\u00020\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\u0006\u001a\u00020\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\u0007\u001a\u00020\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\b\u001a\u00020\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\t\u001a\u00020\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\n\u001a\u00020\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\u000b\u001a\u00020\u0005X\u0082\u0004¢\u0006\u0002\n\u0000R\u0014\u0010\f\u001a\b\u0012\u0004\u0012\u00020\u000e0\rX\u0082\u0004¢\u0006\u0002\n\u0000R\u000e\u0010\u001d\u001a\u00020\u001cX\u0086T¢\u0006\u0002\n\u0000¨\u0006("}, d2 = {"Lcom/ermetic/circuitoshabana/data/Traspasos;", "", "<init>", "()V", "INDICIOS", "Ljava/util/regex/Pattern;", "MOVIDO", "LLEVA", "PERTENECE", "NORMALIZA", "PARCIAL", "CODIGO", "LETRAS_NO_CODIGO", "", "", "contieneIndicios", "", AlarmaCircuito.EXTRA_TEXTO, "codigosEnOrden", "", "fragmento", "oraciones", "esOracionDeTraspaso", "o", "quitarOracionesDeTraspaso", "detectar", "Lcom/ermetic/circuitoshabana/data/ResultadoTraspasos;", "atMs", "", "VIGENCIA_MS", "aplicar", "Lcom/ermetic/circuitoshabana/data/Traspaso;", "actuales", "nuevos", "normalizados", "Lkotlin/Pair;", "ahoraMs", "textoAviso", "t", "haceTexto", "app"}, k = 1, mv = {2, 2, 0}, xi = AndroidUiModes.UI_MODE_NIGHT_MASK)
public final class Traspasos {
    public static final int $stable;
    private static final Pattern CODIGO;
    private static final Pattern INDICIOS;
    public static final Traspasos INSTANCE = new Traspasos();
    private static final Set<String> LETRAS_NO_CODIGO;
    private static final Pattern LLEVA;
    private static final Pattern MOVIDO;
    private static final Pattern NORMALIZA;
    private static final Pattern PARCIAL;
    private static final Pattern PERTENECE;
    public static final long VIGENCIA_MS = 604800000;

    private Traspasos() {
    }

    static {
        Pattern patternCompile = Pattern.compile("(?i)transferid[oa]s?|transfiri[oó]|transfiere|traspas|se integr(?:an|aron)|carga del circuito|llev[aá]ndose|pertenec(?:e|en) actualmente");
        Intrinsics.checkNotNullExpressionValue(patternCompile, "compile(...)");
        INDICIOS = patternCompile;
        Pattern patternCompile2 = Pattern.compile("(?i)transferid[oa]s?|transfiri[oó]|transfiere|traspas\\w*|se integr(?:an|aron)");
        Intrinsics.checkNotNullExpressionValue(patternCompile2, "compile(...)");
        MOVIDO = patternCompile2;
        Pattern patternCompile3 = Pattern.compile("(?i)llev[aá]ndose(?:\\s+(?:parte\\s+de\\s+)?la\\s+carga\\s+del\\s+circuito)?");
        Intrinsics.checkNotNullExpressionValue(patternCompile3, "compile(...)");
        LLEVA = patternCompile3;
        Pattern patternCompile4 = Pattern.compile("(?i)pertenec(?:e|en)\\s+actualmente\\s+al");
        Intrinsics.checkNotNullExpressionValue(patternCompile4, "compile(...)");
        PERTENECE = patternCompile4;
        Pattern patternCompile5 = Pattern.compile("(?i)se\\s+normaliz\\w*|normalizad[oa]s?|se\\s+restablec\\w*");
        Intrinsics.checkNotNullExpressionValue(patternCompile5, "compile(...)");
        NORMALIZA = patternCompile5;
        Pattern patternCompile6 = Pattern.compile("(?i)parte\\s+de|parcial|algunas?\\s+zonas|zonas\\s+del|repartos?|algunos");
        Intrinsics.checkNotNullExpressionValue(patternCompile6, "compile(...)");
        PARCIAL = patternCompile6;
        Pattern patternCompile7 = Pattern.compile("(?<![A-Za-z0-9])([A-Za-z]{1,3})[-\\s]?(\\d{2,4})(?![A-Za-z0-9])");
        Intrinsics.checkNotNullExpressionValue(patternCompile7, "compile(...)");
        CODIGO = patternCompile7;
        LETRAS_NO_CODIGO = SetsKt.setOf((Object[]) new String[]{"Y", "A", "E", "O", "DE", "EL", "LA", "AM", "PM", "HR", "KV", "MW"});
        $stable = 8;
    }

    public final boolean contieneIndicios(String texto) {
        Intrinsics.checkNotNullParameter(texto, "texto");
        return INDICIOS.matcher(texto).find();
    }

    public final List<String> codigosEnOrden(String fragmento) {
        Intrinsics.checkNotNullParameter(fragmento, "fragmento");
        Matcher matcher = CODIGO.matcher(fragmento);
        LinkedHashSet linkedHashSet = new LinkedHashSet();
        while (matcher.find()) {
            String strGroup = matcher.group(1);
            Intrinsics.checkNotNull(strGroup);
            String upperCase = strGroup.toUpperCase(Locale.ROOT);
            Intrinsics.checkNotNullExpressionValue(upperCase, "toUpperCase(...)");
            if (!LETRAS_NO_CODIGO.contains(upperCase)) {
                linkedHashSet.add(upperCase + matcher.group(2));
            }
        }
        return CollectionsKt.toList(linkedHashSet);
    }

    private final List<String> oraciones(String texto) {
        List listSplit$default = StringsKt.split$default((CharSequence) texto, new char[]{'\n', '.', ';'}, false, 0, 6, (Object) null);
        ArrayList arrayList = new ArrayList(CollectionsKt.collectionSizeOrDefault(listSplit$default, 10));
        Iterator it = listSplit$default.iterator();
        while (it.hasNext()) {
            arrayList.add(StringsKt.trim((CharSequence) it.next()).toString());
        }
        ArrayList arrayList2 = new ArrayList();
        for (Object obj : arrayList) {
            if (((String) obj).length() > 0) {
                arrayList2.add(obj);
            }
        }
        return arrayList2;
    }

    private final boolean esOracionDeTraspaso(String o) {
        return INDICIOS.matcher(o).find();
    }

    public final String quitarOracionesDeTraspaso(String texto) {
        Intrinsics.checkNotNullParameter(texto, "texto");
        List listSplit$default = StringsKt.split$default((CharSequence) texto, new char[]{'\n'}, false, 0, 6, (Object) null);
        ArrayList arrayList = new ArrayList();
        for (Object obj : listSplit$default) {
            String str = (String) obj;
            Traspasos traspasos = INSTANCE;
            if (traspasos.esOracionDeTraspaso(str)) {
                List<String> listOraciones = traspasos.oraciones(str);
                if (!(listOraciones instanceof Collection) || !listOraciones.isEmpty()) {
                    Iterator<T> it = listOraciones.iterator();
                    while (it.hasNext()) {
                        if (!INSTANCE.esOracionDeTraspaso((String) it.next())) {
                        }
                    }
                }
            }
            arrayList.add(obj);
        }
        return CollectionsKt.joinToString$default(arrayList, "\n", null, null, 0, null, new Function1() { // from class: com.ermetic.circuitoshabana.data.Traspasos$$ExternalSyntheticLambda0
            @Override // kotlin.jvm.functions.Function1
            public final Object invoke(Object obj2) {
                return Traspasos.quitarOracionesDeTraspaso$lambda$5((String) obj2);
            }
        }, 30, null);
    }

    static final CharSequence quitarOracionesDeTraspaso$lambda$5(String linea) {
        Intrinsics.checkNotNullParameter(linea, "linea");
        Traspasos traspasos = INSTANCE;
        if (!traspasos.esOracionDeTraspaso(linea)) {
            return linea;
        }
        List<String> listOraciones = traspasos.oraciones(linea);
        ArrayList arrayList = new ArrayList();
        for (Object obj : listOraciones) {
            if (!INSTANCE.esOracionDeTraspaso((String) obj)) {
                arrayList.add(obj);
            }
        }
        return CollectionsKt.joinToString$default(arrayList, ". ", null, null, 0, null, null, 62, null);
    }

    /* JADX WARN: Code duplicated, block: B:105:0x01e5 A[SYNTHETIC] */
    /* JADX WARN: Code duplicated, block: B:107:0x01a7 A[SYNTHETIC] */
    /* JADX WARN: Code duplicated, block: B:110:0x01d5 A[SYNTHETIC] */
    /* JADX WARN: Code duplicated, block: B:112:0x01c2 A[SYNTHETIC] */
    /* JADX WARN: Code duplicated, block: B:57:0x01ad  */
    /* JADX WARN: Code duplicated, block: B:60:0x01c8  */
    public final ResultadoTraspasos detectar(String texto, long atMs) {
        long j;
        ArrayList arrayList;
        ArrayList arrayList2;
        Intrinsics.checkNotNullParameter(texto, "texto");
        if (!contieneIndicios(texto)) {
            return new ResultadoTraspasos(CollectionsKt.emptyList(), CollectionsKt.emptyList());
        }
        ArrayList arrayList3 = new ArrayList();
        LinkedHashSet linkedHashSet = new LinkedHashSet();
        for (String str : oraciones(texto)) {
            String str2 = str;
            boolean zFind = PARCIAL.matcher(str2).find();
            Matcher matcher = PERTENECE.matcher(str2);
            if (matcher.find()) {
                String strSubstring = str.substring(0, matcher.start());
                Intrinsics.checkNotNullExpressionValue(strSubstring, "substring(...)");
                List<String> listCodigosEnOrden = codigosEnOrden(strSubstring);
                String strSubstring2 = str.substring(matcher.end());
                Intrinsics.checkNotNullExpressionValue(strSubstring2, "substring(...)");
                List<String> listCodigosEnOrden2 = codigosEnOrden(strSubstring2);
                if (!listCodigosEnOrden.isEmpty() && !listCodigosEnOrden2.isEmpty()) {
                    for (String str3 : listCodigosEnOrden) {
                        ArrayList arrayList4 = new ArrayList();
                        for (Object obj : listCodigosEnOrden2) {
                            if (!Intrinsics.areEqual((String) obj, str3)) {
                                arrayList4.add(obj);
                            }
                        }
                        arrayList3.add(new Traspaso(str3, arrayList4, zFind, atMs));
                    }
                }
                j = atMs;
            } else {
                j = atMs;
                Matcher matcher2 = LLEVA.matcher(str2);
                if (matcher2.find()) {
                    String strSubstring3 = str.substring(0, matcher2.start());
                    Intrinsics.checkNotNullExpressionValue(strSubstring3, "substring(...)");
                    List<String> listCodigosEnOrden3 = codigosEnOrden(strSubstring3);
                    String strSubstring4 = str.substring(matcher2.end());
                    Intrinsics.checkNotNullExpressionValue(strSubstring4, "substring(...)");
                    List<String> listCodigosEnOrden4 = codigosEnOrden(strSubstring4);
                    if (!listCodigosEnOrden3.isEmpty() && !listCodigosEnOrden4.isEmpty()) {
                        for (String str4 : listCodigosEnOrden4) {
                            ArrayList arrayList5 = new ArrayList();
                            for (Object obj2 : listCodigosEnOrden3) {
                                if (!Intrinsics.areEqual((String) obj2, str4)) {
                                    arrayList5.add(obj2);
                                }
                            }
                            arrayList3.add(new Traspaso(str4, arrayList5, zFind, j));
                        }
                    }
                } else {
                    Matcher matcher3 = MOVIDO.matcher(str2);
                    if (matcher3.find()) {
                        String strSubstring5 = str.substring(0, matcher3.start());
                        Intrinsics.checkNotNullExpressionValue(strSubstring5, "substring(...)");
                        List<String> listCodigosEnOrden5 = codigosEnOrden(strSubstring5);
                        String strSubstring6 = str.substring(matcher3.end());
                        Intrinsics.checkNotNullExpressionValue(strSubstring6, "substring(...)");
                        List<String> listCodigosEnOrden6 = codigosEnOrden(strSubstring6);
                        if (listCodigosEnOrden5.isEmpty() || listCodigosEnOrden6.isEmpty()) {
                            if (listCodigosEnOrden5.isEmpty() && listCodigosEnOrden6.size() >= 2) {
                                listCodigosEnOrden5 = CollectionsKt.listOf(CollectionsKt.first((List) listCodigosEnOrden6));
                                listCodigosEnOrden6 = CollectionsKt.drop(listCodigosEnOrden6, 1);
                                for (String str5 : listCodigosEnOrden5) {
                                    arrayList = new ArrayList();
                                    for (Object obj3 : listCodigosEnOrden6) {
                                        if (!Intrinsics.areEqual((String) obj3, str5)) {
                                            arrayList.add(obj3);
                                        }
                                    }
                                    arrayList2 = arrayList;
                                    if (!arrayList2.isEmpty()) {
                                        arrayList3.add(new Traspaso(str5, arrayList2, zFind, j));
                                    }
                                }
                            }
                        } else {
                            while (r14.hasNext()) {
                                arrayList = new ArrayList();
                                while (r2.hasNext()) {
                                    if (!Intrinsics.areEqual((String) obj3, str5)) {
                                        arrayList.add(obj3);
                                    }
                                }
                                arrayList2 = arrayList;
                                if (!arrayList2.isEmpty()) {
                                    arrayList3.add(new Traspaso(str5, arrayList2, zFind, j));
                                }
                            }
                        }
                    } else if (NORMALIZA.matcher(str2).find()) {
                        linkedHashSet.addAll(codigosEnOrden(str));
                    }
                }
            }
            atMs = j;
        }
        ArrayList arrayList6 = new ArrayList();
        for (Object obj4 : arrayList3) {
            if (!linkedHashSet.contains(((Traspaso) obj4).getOrigen())) {
                arrayList6.add(obj4);
            }
        }
        HashSet hashSet = new HashSet();
        ArrayList arrayList7 = new ArrayList();
        for (Object obj5 : arrayList6) {
            if (hashSet.add(((Traspaso) obj5).getClave())) {
                arrayList7.add(obj5);
            }
        }
        return new ResultadoTraspasos(arrayList7, CollectionsKt.toList(linkedHashSet));
    }

    public final List<Traspaso> aplicar(List<Traspaso> actuales, List<Traspaso> nuevos, List<Pair<String, Long>> normalizados, long ahoraMs) {
        Intrinsics.checkNotNullParameter(actuales, "actuales");
        Intrinsics.checkNotNullParameter(nuevos, "nuevos");
        Intrinsics.checkNotNullParameter(normalizados, "normalizados");
        LinkedHashMap linkedHashMap = new LinkedHashMap();
        for (Traspaso traspaso : CollectionsKt.plus((Collection) actuales, (Iterable) nuevos)) {
            Traspaso traspaso2 = (Traspaso) linkedHashMap.get(traspaso.getOrigen());
            if (traspaso2 == null || traspaso.getAtMs() >= traspaso2.getAtMs()) {
                linkedHashMap.put(traspaso.getOrigen(), traspaso);
            }
        }
        Collection collectionValues = linkedHashMap.values();
        Intrinsics.checkNotNullExpressionValue(collectionValues, "<get-values>(...)");
        ArrayList arrayList = new ArrayList();
        for (Object obj : collectionValues) {
            Traspaso traspaso3 = (Traspaso) obj;
            if (ahoraMs - traspaso3.getAtMs() <= 604800000) {
                List<Pair<String, Long>> list = normalizados;
                if (!(list instanceof Collection) || !list.isEmpty()) {
                    Iterator<T> it = list.iterator();
                    while (true) {
                        if (it.hasNext()) {
                            Pair pair = (Pair) it.next();
                            String str = (String) pair.component1();
                            long jLongValue = ((Number) pair.component2()).longValue();
                            if (Intrinsics.areEqual(str, traspaso3.getOrigen()) && jLongValue >= traspaso3.getAtMs()) {
                                break;
                            }
                        }
                    }
                }
                arrayList.add(obj);
                break;
            }
        }
        return arrayList;
    }

    public final String textoAviso(Traspaso t, String haceTexto) {
        String str;
        String origen;
        StringBuilder sb;
        Intrinsics.checkNotNullParameter(t, "t");
        Intrinsics.checkNotNullParameter(haceTexto, "haceTexto");
        if (t.getDestinos().size() == 1) {
            str = (String) CollectionsKt.first((List) t.getDestinos());
        } else {
            str = CollectionsKt.joinToString$default(CollectionsKt.dropLast(t.getDestinos(), 1), ", ", null, null, 0, null, null, 62, null) + " y " + CollectionsKt.last((List) t.getDestinos());
        }
        if (t.getParcial()) {
            origen = t.getOrigen();
            sb = new StringBuilder("parte de la carga del circuito ");
        } else {
            origen = t.getOrigen();
            sb = new StringBuilder("el circuito ");
        }
        return "Parece que " + sb.append(origen).append(" pasó").toString() + " " + (t.getDestinos().size() == 1 ? new StringBuilder("al circuito ") : new StringBuilder("a los circuitos ")).append(str).toString() + " " + haceTexto + ". Si " + t.getOrigen() + " no coincide con tus apagones, prueba con " + str + ".";
    }
}
